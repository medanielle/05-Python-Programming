import bankacct_class

def first():
    #get starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create a bank account object
    savings = bankacct_class.BankAccount(start_bal)

    # Deposit user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that in your account')
    savings.deposit(pay)

    # Display the balance
    print(f'\nHere is your balance: ${savings.get_balance():,.2f}')
    # print('\nHere is your balance: $'.format(savings.get_balance(), ',.2f'))

    # Withdrawl amount
    withdraw = float(input('How much do you want to withdraw? '))
    print('I will remove that in your account')
    savings.withdraw(withdraw)

    # Display the balance
    print(f'\nHere is your balance: ${savings.get_balance():,.2f}')

# call the main func
#first()

def second():
    # get starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create a bank account object
    savings = bankacct_class.BankAccount(start_bal)

    # Deposit user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that in your account')
    savings.deposit(pay)

    # Display the balance
    print(savings)
    # print('\nHere is your balance: $'.format(savings.get_balance(), ',.2f'))

    # Withdrawl amount
    withdraw = float(input('How much do you want to withdraw? '))
    print('I will remove that in your account')
    savings.withdraw(withdraw)

    # Display the balance
    print(savings)

second()