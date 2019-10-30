def firstExample():
    print(f'Hello {get_name()}!')
    return

def get_name():
    return input("Enter your name: ")

#firstExample()

def scopeExample():
    texas()
    california()

def texas():
    birds = 5000
    print(f'Texas has {birds} birds')

def california():
    birds = 8000
    print(f'California has {birds} birds')

#scopeExample()

def argumentExample():
    #demo of argument being passed to a function
    value = 5
    show_double(value)

def show_double(p_value):
    result = p_value *2
    print(result)

#argumentExample()

def multipleArguments():
    #demo of func with multiple arguments
    print('The sum of 12 and 45 is', show_sum(12, 45))
    

def show_sum(p_num1, p_num2):
    return p_num1 + p_num2

#multipleArguments()

def twoStringArg():
    #demo shows passing two string arguments to a func
    first_name = 'daniel'
    last_name = 'teacher'
    print('your name reverse is ')
    name_swap(first_name, last_name)

def name_swap(first, last):
    print(last, first)

#twoStringArg()

def keywordArguments():
    #demos key word arguments
    #show simple interest
    show_interest(10000.0, 0.01, 10)

def show_interest(p_principal, p_rate, p_period):
    interest = p_principal * p_rate * p_period
    print('the simple interest will be $', format(interest, ',.2f'), sep='')

#keywordArguments()

number = 0
def globalVarExample():
    global number
    number = int(input("Enter a number: "))
    shownumber()

def shownumber():
    print(f'The number your entered was {number}')

#globalVarExample()



