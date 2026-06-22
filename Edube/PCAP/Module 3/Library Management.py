
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed")
        else:
            print(f"{self.title} is unavailable")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned")


python_book = Book("Python Basics")

python_book.borrow()
python_book.borrow()
python_book.return_book()
python_book.borrow()