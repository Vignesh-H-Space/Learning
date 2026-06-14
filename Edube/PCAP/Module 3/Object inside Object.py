class Engine:
    def __init__(self):
        self.power = 100

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()

print(c.engine.power)