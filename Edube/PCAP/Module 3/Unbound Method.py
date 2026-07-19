class Zombie:
    def __new__(cls):
        print("Zombie Created!")
        
    def __init__(self):
        self.brains = 0
        print("Zombie Initialized!")

z = Zombie()

print(type(z))
