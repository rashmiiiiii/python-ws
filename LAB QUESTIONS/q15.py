class Account:
    def __init__(self,acno,name,balance):
        self.acno = acno
        self.name = name
        self.balance = balance
        

    def deposit(self,deposit1):
        self.balance += deposit1
        print(f"after increment of salary {self.balance}")
    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount
        print(f"after withdrawal from salary {self.balance}")
    def showInfo(self):
        print(f"account number:{self.acno}\nname:{self.name}\nbalance:{self.balance}")

ac1 =Account(10850,"rajath",5689)
ac1.deposit(2500)
ac1.showInfo()
ac1.withdraw(500)
ac1.showInfo()



