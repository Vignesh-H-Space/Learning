class Duck:
    def speak(self): return "Quack"

class Dog:
    def speak(self): return "Woof"

class Cat:
    def purr(self): return "Meow"

animals = [Duck(), Dog(), Cat()]
sounds = []

for animal in animals:
    try:
        sounds.append(animal.speak())
    except AttributeError:
        sounds.append("Silent")

print(sounds)
