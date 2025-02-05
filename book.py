class Book:
    def __init__(self):
        self.books = []

    def add_book(self):
        isbn = input("Type in your ISBN: ")
        title = input("What is your title: ")
        author = input("What is the author's name: ")
        if any(book[0] == isbn for book in self.books):
            print("Book with this ISBN already exists.")
        else:
            self.books.append((isbn, title, author))
            print(f"Book '{title}' added successfully.")

    def remove_book(self):
        isbn = input(
            "Type in the ISBN number of the book you want to remove: ")
        for book in self.books:
            if book[0] == isbn:
                self.books.remove(book)
                print(f"Book '{book[1]}' removed successfully.")
                return
        print("Book not found.")

    def print_books(self):
        if not self.books:
            print("No books available.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(
                    f"Book {idx}: {book[1]} - Author: {book[2]} (ISBN: {book[0]})")

    def total_books(self):
        print(f"Total number of books: {len(self.books)}")


def main():
    library = Book()
    library.books = [
        ("978-0-306", "Introduction to Algorithms", "Thomas H. Cormen"),
        ("978-0-672", "Python Crash Course", "Eric Matthes"),
        ("978-0-079", "Clean Code", "Robert C. Martin"),
        ("978-1-491", "Deep Learning", "Ian Goodfellow"),
        ("978-0-321", "The Pragmatic Programmer", "Andrew Hunt"),
    ]

    while True:
        print("Select action:")
        print("\t1 = Print books")
        print("\t2 = Add book")
        print("\t3 = Remove book")
        print("\t4 = Total number of books")
        print("\t5 = Stop")

        selection = input("> ")

        if selection == "1":
            library.print_books()
        elif selection == "2":
            library.add_book()
        elif selection == "3":
            library.remove_book()
        elif selection == "4":
            library.total_books()
        else:
            break


if __name__ == "__main__":
    main()
