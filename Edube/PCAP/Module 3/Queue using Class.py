class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.items)