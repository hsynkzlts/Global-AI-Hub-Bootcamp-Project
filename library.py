
class Library:

    # "books.txt" dosyasını açar
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    # "books.txt" dosyasını kapar
    def __del__(self):
        self.file.close()

    # kitap listesini ekrana yazdırır
    def list_books(self):
        books = []
        with open(self.file_name, "r") as f:
            for line in f:
                books.append(line.strip().split(","))
        for book in books:
            print(f"Title: {book[0]}, Author: {book[1]}")
            
    # Kullanıcıdan kitap bilgilerini alıp "books.txt" dosyasına eklediğimiz kod bloğu
    # title, author, release_year, pages bilgileri kullanıcıdan alınır
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}"
        self.file.write(f"\n{book_info}")

    # Kullanıcıdan ismi alınan kitabı "books.txt" dosyasından siler, kitap ismi yoksa hata kodunu döndürür
    def remove_book(self):
        title = input("Enter title of book to remove: ")
        books = []
        with open(self.file_name, "r") as f:
            for line in f:
                books.append(line.strip())
        try:
            index = books.index(f"{title},")
            books.pop(index)
            with open(self.file_name, "w") as f:
                f.writelines(books)
        except ValueError:
            print("Book not found.")

    # Kitap adına, yazara veya yayımlanma yılına göre kitap arama yapar. (Ekstra özellik)
    def search_books(self, search_term):
        books = []
        with open(self.file_name, "r") as f:
            for line in f:
                book_info = line.strip().split(",")
                if search_term.lower() in (info.lower() for info in book_info):
                    books.append(book_info)
        return books



if __name__ == "__main__":
    lib = Library()

    # Menü döngüsü, arama özelliğini de ekleyerek buna göre düzenledim
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Search Books")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            search_term = input("Enter search term: ")
            books = lib.search_books(search_term)
            if books:
                print("Found books:")
                for book in books:
                    print(f"Title: {book[0]}, Author: {book[1]}")
            else:
                print("No books found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
