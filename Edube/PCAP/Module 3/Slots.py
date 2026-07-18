class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)

try:
    p.z = 30
    print("Successfully Added Z!")
    
except AttributeError:
    print("Caught an AttributeError!")