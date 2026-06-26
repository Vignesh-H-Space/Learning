class Dog:
    tricks = []  # Look closely at where this is defined!

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
