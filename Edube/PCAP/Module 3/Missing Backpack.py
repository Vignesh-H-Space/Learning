class Animal:
    def __init__(self):
        self.species = "Mammal"

class Dog(Animal):
    def __init__(self):
        self.sound = "Woof"

my_dog = Dog()


print(hasattr(my_dog, 'sound'))
print(hasattr(my_dog, 'species'))