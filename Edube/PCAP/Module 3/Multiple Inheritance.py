class Mom:
    def eyes(self):
        return "Brown"

class Dad:
    def eyes(self):
        return "Blue"

class Child(Mom, Dad):
    pass

kid = Child()

print(kid.eyes())