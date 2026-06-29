class Grandparent:
    def __init__(self):
        self.age = 80

class Parent(Grandparent):
    def __init__(self):
        # Notice what is missing here!
        self.money = 100
        
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.toys = 10
kid = Child()

print(hasattr(kid, 'toys'))
print(hasattr(kid, 'money'))
print(hasattr(kid, 'age'))