class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("Max")
d2 = Dog("Rocky")

d1.name = "Buddy"

print(d1.name)
print(d2.name)