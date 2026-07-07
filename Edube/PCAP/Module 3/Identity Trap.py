class Appliance: 
    pass

class Microwave(Appliance): 
    pass

class SmartMicrowave(Microwave): 
    pass

my_oven = Microwave()

print(issubclass(SmartMicrowave, Appliance))
print(isinstance(my_oven, Appliance))
print(isinstance(my_oven, SmartMicrowave))