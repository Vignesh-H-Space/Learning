class Bank:
    def __init__(self):
        self.balance = 100

    def deposit(self, amount):
        self.balance += amount

b = Bank()

b.deposit(50)
b.deposit(20)

print(b.balance)