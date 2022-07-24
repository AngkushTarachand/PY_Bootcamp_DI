class BankAccount:
    def __int__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount_deposit):
        if amount_deposit < 0 and self.authenticated is False:
            raise Exception("Sorry, you cannot deposit an negative integer")
        else:
            self.balance += amount_deposit
            print("The amount cannot be deposited.")

    def withdraw(self, withdraw):
        if withdraw > self.balance and self.authenticated is False:
            raise Exception("Sorry, you cannot withdraw an amount inferior your balance" )
        else:
            self.balance - withdraw

    def authenticate(self, username1, password1):
        if self.username is not username1:
            raise Exception("Username incorrect")
        elif self.password is not password1:
            raise Exception("Password incorrect")
        elif self.password is password1 and self.username is username1:
            self.authenticated = True


class MinimumBalanceAccount(BankAccount):
    def __int__(self, username, password, authenticated, minimum_balance=0):
        self.minimum_balance = minimum_balance

    def withdraw(self, withdraw):
        if self.minimum_balance < withdraw:
            raise Exception("Cannot withdraw an amount greater than minimum balance mount")
        else:
            self.minimum_balance - withdraw










