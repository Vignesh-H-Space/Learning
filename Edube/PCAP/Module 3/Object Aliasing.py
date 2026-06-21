class Box:
    def __init__(self, value):
        self.value = value

b1 = Box(10)
b2 = b1

b2.value += 5

print(b1.value)
print(b2.value)
