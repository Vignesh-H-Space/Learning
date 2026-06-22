class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1

    def display(self):
        print(Counter.total)


a = Counter()
b = Counter()
c = Counter()

a.display()
b.display()