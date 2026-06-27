class Parent:
    def __init__(self):
        self.money = 1000

class Child(Parent):
    def __init__(self):
        self.toys = 5
        
kid = Child()

print(hasattr(kid, 'toys'))
print(hasattr(kid, 'money'))
