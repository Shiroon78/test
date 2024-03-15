class Library:
    def __init__(self):
        self.noofbooks = 0
        self.book = []
    
    def add_book(self, book):
        self.book.append(book)
        self.noofbooks += 1
    
    def showInfo(self):
        print(f"The library has {self.noofbooks} books, The books are")
        for book in self.book:
            print(book)


li = Library()
li.add_book("Harry Potter")
li.add_book("Law of pythsics")
li.add_book("Plannet 2")
li.showInfo()
    