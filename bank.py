class Bank_Account:
    def __init__(self):
     self.balance=0
    print("Hello!!!Welcome to the withdrawel and depositing machine")

    def deposit(self):
        amount=float(input("Enter the amount to be deposited"))
        self.balance += amount
        print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount=float(input("Enter the amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You withdrew:",amount)
        else:
            print("\n Insufficient balance")

    def display(self):
        print("\n Net Available Balance=",self.balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()

