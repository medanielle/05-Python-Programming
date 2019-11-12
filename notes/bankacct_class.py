# the BankAccount class simulates a Bank Account

# values = attributes

# classes encapsulate all the attributes and functions??

class BankAccount:
    
    # the __int__ method accepts an argument for the account's balance. It is assigned to the __balance attribute

    def __init__(self, bal):
        self.__balance = bal

    # the deposit method makes a deposit into the account
    def deposit(self, amt):
        self.__balance += amt
    
    # the withdraw method withdraws an amount from the account
    def withdraw(self, amt):
        if self.__balance >= amt:
            self.__balance -= amt
        else:
            print('Error: Insufficient Funds')

    # the get_balance method returns the account balance
    def get_balance(self):
        return self.__balance

#second()
    # the __str__ method returns a string indicating the object's state
    # autmatically called when you pass objext to print function
    def __str__(self):
        return f'The balance is ${self.__balance:,.2f}'