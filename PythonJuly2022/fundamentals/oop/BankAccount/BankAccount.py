# Not complete will review in code review--just not grasping the idea

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(f"Balance:{self.balance}")
    def withdraw(self, amount):
        self.amount=amount
        if self.amount>self.balance:
            print(f"Insuffuicient Funds: {self.balance}")
        else:
            self.balance=self.balance-self.amount
            print(f"New Balance: {self.balace}")
    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
    def yield_interest(self):
        self.interest_yeild=interest_yeild


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.amount=amount

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    print(self.account.balance)		# or access its attributes

