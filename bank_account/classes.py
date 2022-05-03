
class Account():
    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # print(f"Deposit Accepted.\nCurrent Balance: {self.balance}")

    def withdraw(self, amount):
        total = self.balance
        total -= amount
        if total <= 0:
            print(f"Withdrawal Rejected\nCurrent Balance: {self.balance}")
        else:
            print(f"Withdrawal Accepted\nNew Balance: {self.balance}")
            self.balance -= amount

    def __str__(self):
        return f"Owner: {self.first} {self.last}, Balance: {self.balance}"
