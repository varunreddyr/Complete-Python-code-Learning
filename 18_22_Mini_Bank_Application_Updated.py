import sys


class Customer:
    """This class, developed by Varun, describes bank operations."""
    bank_name = 'VARUNBANK'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('After deposit, balance is:', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds....")
            sys.exit()
        else:
            self.balance -= amount
            print("After withdrawal, balance:", self.balance)


print("Welcome to", Customer.bank_name)
name = input("Enter your name: ")
c = Customer(name)

while True:
    print(" d-Deposit\n w-Withdraw \n e-Exit")
    option = input("Choose your option: ").lower()

    if option == 'd':
        amount_str = input("Enter amount: ")
        # Ensuring the input is a valid float number
        if amount_str.replace('.', '', 1).isdigit():
            amount = float(amount_str)  # Convert the valid input to float
            c.deposit(amount)
        else:
            print("Please enter the correct amount.")

    elif option == 'w':
        amount_str = input("Enter amount to withdraw: ")
        # Ensuring the input is a valid float number
        if amount_str.replace('.', '', 1).isdigit():
            amount = float(amount_str)  # Convert the valid input to float
            c.withdraw(amount)
        else:
            print("Please enter the correct amount.")

    elif option == 'e':
        print('Thanks for banking with us... Have a nice day!')
        sys.exit()
    else:
        print('Invalid option... Please choose a valid option.')