class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def display(self):
        print(self.count)

c1 = Counter()
c2 = Counter()

c1.increase()
c1.increase()

c2.increase()

c1.display()
c2.display()