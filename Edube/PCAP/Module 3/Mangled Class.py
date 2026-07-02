class Parent:
    def __init__(self):
        self.__money = 1000

    def get_parent_money(self):
        return self.__money

class Child(Parent):
    def __init__(self):
        # Successfully build the parent's variables
        Parent.__init__(self)
        
        # The child tries to overwrite the private money variable!
        self.__money = 500  