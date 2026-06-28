class Grandparent:
    def __init__(self):
        self.age = 80

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.toys = 10
