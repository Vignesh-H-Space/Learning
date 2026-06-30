class Test:
    def __init__(self):
        self.a = 1
        b = 2
        self.c = 3

t = Test()

# Adding a variable on the fly
t.d = 4

print(len(t.__dict__))