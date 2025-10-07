class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)

    def deposit(self, amount):
        self.balance += int(amount)
        print(f"{self.owner}, {amount}$ was added to your account. Your Balance: {self.balance}$")

    def withdraw(self, amount):
        self.balance -= int(amount)

        if self.balance < amount:
            print("Insufficient funds")
        else:
            print(f"{self.owner}, you have withdrawn -{amount}$ from your account. Your Balance: {self.balance}$")
    
    def get_balance(self):
        if self.balance < 0:
            return
        else:
            print(f"{self.owner}, your account balance is {self.balance}$")

  
 
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = int(interest_rate)

    def apply_interest(self):
        if self.balance < 0:
            return
        
        if self.balance > 50:
            interest = self.balance * (self.interest_rate / 100)
            self.balance -= int(interest)
            print(f"{self.owner}, {int(interest)}$ was added to your account savings from your balance. Your balance: {self.balance}")

        else:
            print(f"{self.owner}, Your balance is too low for savings")



savings = SavingsAccount("Anna", 102, 5)
savings.deposit(13)
savings.withdraw(35)
savings.get_balance()
savings.apply_interest()

        