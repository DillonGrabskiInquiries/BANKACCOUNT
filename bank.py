class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate
            return self

michael = User("michael", "michael.com")
anna = User("anna", "anna.com")

michael.account.deposit(500).deposit(500).deposit(500).withdraw(100).yield_interest()

anna.account.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest()
