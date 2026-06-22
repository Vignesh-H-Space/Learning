
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

