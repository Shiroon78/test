# Library Management 

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def print_books(self):
        print("Total number of books:", self.no_of_books)
        print("Books:")
        for book in self.books:
            print(book)

    def __del__(self):
        print("Deleting the library object")

# Create a library object
library = Library()

# Add some books
library.add_book("Python Crash Course")
library.add_book("Fluent Python")

# Print all books and the number of books
library.print_books()
print()

# Add a new book
library.add_book("Effective Python")

# Print all books and the number of books again
library.print_books()

# Delete the library object
del library