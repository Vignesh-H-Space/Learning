class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 20

c1 = Car("BMW")
c2 = Car("Audi")

c1.accelerate()
c1.accelerate()

c2.accelerate()

print(c1.brand, c1.speed)
print(c2.brand, c2.speed)