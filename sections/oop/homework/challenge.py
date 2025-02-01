class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry, not enough funds")

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"


a = Account("Sam", 500)

print(a)
print(a.owner)
print(a.balance)
a.deposit(500)
print(a.balance)
a.withdrawal(800)
print(a.balance)
a.withdrawal(300)
print(a.balance)
