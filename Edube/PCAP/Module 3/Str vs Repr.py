class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # __repr__ is meant for developers to see the "raw" object
        return f"REPR: {self.name}"

box = Item("Shoes")

print(str(box))
print(repr(box))
