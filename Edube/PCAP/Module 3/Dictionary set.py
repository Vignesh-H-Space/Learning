class Coin:
    def __init__(self, value):
        self.value = value
        
    def __eq__(self, other):
        return self.value == other.value
        
    def __hash__(self):
        return hash(self.value)

c1 = Coin(25)
c2 = Coin(25)

pocket = {c1, c2}

print(len(pocket))