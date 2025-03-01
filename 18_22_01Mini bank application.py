#Mini bank application:
import sys
class customer:
    '''This class Developed by varun and describes bank operation'''
    bankname='VARUNBANK'
    def __init__(self,name,balance=0.0): #Here balance=0.0 is default argument
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('After deposit,balance is:',self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds....")
            sys.exit()
        else:
            self.balance=self.balance-amount
            print("after withdraw,balance:",self.balance)
print("Welcome to ",customer.bankname)
name=input("Enter your name:")
c=customer(name)
while True:
    print(" d-Deposit\n w-withdraw \n e-exit")
    option =input("Choose your option:")
    if option.lower()=='d':
        amount=float(input("Enter amount:"))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount ot withdraw'))
        c.withdraw(amount)

    elif option.lower()=='e':
        print('Thanks for Banking...Have A Nice Day')
        sys.exit()
    else:
        print('Invalid option...Please choose the valid option')





