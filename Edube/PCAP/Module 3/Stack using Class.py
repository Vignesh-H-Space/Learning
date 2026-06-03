class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

s = Stack()
s.push(10)
s.push(20)
print(s.items)