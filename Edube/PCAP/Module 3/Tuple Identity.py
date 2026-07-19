class Vehicle: 
    pass

class Car(Vehicle): 
    pass

class Boat: 
    pass

my_car = Car()

check_1 = isinstance(my_car, (Boat, Vehicle))

check_2 = issubclass(Car, (Boat, int))

print(check_1)
print(check_2)
