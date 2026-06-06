class Queue:
    def __init__(self):
        self.items = ["A", "B", "C"]

    def dequeue(self):
        return self.items.pop(0)

