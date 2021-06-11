class BankAccount:

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        int_rate = 0
        balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance
            return self

michaelAccount = BankAccount(8, 100)
annaAccount = BankAccount(9, 100)

michaelAccount.deposit(500).deposit(500).deposit(500).withdraw(100).yield_interest()

annaAccount.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()
