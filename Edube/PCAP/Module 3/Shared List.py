class Dog:
    tricks = []  # Look closely at where this is defined!

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("Fido")
dog2 = Dog("Buddy")

dog1.add_trick("Roll over")
dog2.add_trick("Play dead")

# What does this print?
print(dog1.tricks)

