class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration  

        self.start -= 1
        return self.start

timer = Countdown(3)

for num in timer:
    print(num)
