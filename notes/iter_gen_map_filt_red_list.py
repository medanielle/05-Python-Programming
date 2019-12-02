# Python iterator   (found under Functions on GitHub)

# iterator used on lists, or tuple, etc

my_list= [1,2,3,4]
def my_for():
    for item in my_list:
        print(item)

#my_for()

def traverse(iterable):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break

#traverse(my_list)

def my_next():
    L1 = [1,2,3]
    it = iter(L1)
    print(it.__next__())
    print(it.__next__())
    #print(it.__next__())
    #print(it.__next__())
    #print(it.__next__())
    print(next(it))
    print(next(it))
    # output after 3 => StopIteration
    
# my_next()
# iter(100)  Output=> TypeError: 'int' object is not iterable

# Python Generator

def my_gen():
    print('First item')
    print('more of the first')
    print('even more')
    yield 10
    #return => can't have it a return, otherwise it will stop the generator

    print('second item')
    yield 20

    print('third item')
    yield # removed 30 and it prints None

# gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(gen)  Output +> <generator object my_gen at 0x0000021CBB5D19E0>



# A Python program to generate squares from 1 to 100 using yield and therefore generator   
# An infinite generator function that prints next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes from this point      
  
# Driver code to test above generator function 
def another_gen():
    for num in nextSquare(): 
        if num > 100: 
            break    
        print(num)



# Map function
# calls the specified function and then applies it each item of an iterable

def square(x):
    return x*x

def my_map():
    numbers = [1,2,3,4,5]
    sqr_list = map(square, numbers)
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))
    # next(sqr_list)

my_map()

# lambda functions
# temporary one liner anonymous functions (can't call again after it is used)

def my_lambda():
    square = lambda x: x*x
    print(square(5))
    print(square(6))

    sum = lambda x, y, z: x + y + z
    print(sum(5, 10, 15))
    
# my_lambda()

def map_lambda():
    numbers = [1,2,3,4,5]
    sqr_list = map(lambda x: x*x, numbers)
    #print(sqr_list)     output => <map object at 0x000001BB171CEA60>
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))
    print(next(sqr_list))

# map_lambda()

def new_map():
    tens = [10, 20, 30, 40, 50]
    indx = [1, 2, 3, 4]
    powers = list(map(pow, tens, reversed(indx)))
    print(powers)

# new_map()

# Filter
# Takes in 2 arguments, function and iterable
# only returns items in the list that are True 

def isPrime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
    return True
# prime function is bad lol

def my_filter():
    filter_object = filter(isPrime, range(10))
    print('Prime numbers between 1-10', list(filter_object))

# my_filter()

def filter_lambda():
    # is even example
    filter_object = filter(lambda x: x % 2 ==0, range(10))
    print(list(filter_object))

# filter_lambda()

def new_filter():
    # filter on random list w/o function
    randomList = [1,'a', 0, False, True, '0']
    filteredList = filter(None, randomList)

    print('Filtered: ')
    for element in filteredList:
        print(element)
    # 0 and False are Filtered out with no function since they resolve as False

# new_filter()

# Reduce

# receives two arguments, function and iterable
# returns a single value
# good for rolling computation to sequential pairs of values in a list

# reduce comes from the functools module
import functools

# define our function
def mult(x,y):
    print('x =', x, 'y =', y)
    return x*y

# apply reduce to our function
def factorial():
    fact = functools.reduce(mult, range(1,4))
    print('Factorial of 3 is ', fact)

#factorial()

def more_reduce():
    product1 = 1
    listy = [1, 2, 3, 4]
    for num in listy:
        product1 *= num
        print(f'Num: {num} \t product : {product1}')
        print(product1)

    product2 = functools.reduce((lambda x, y: x*y), listy)
    print(product2)

    sum_num = functools.reduce((lambda x, y: x+y), listy)
    print(sum_num)

# more_reduce()

# List Comprehension

# Good way to create a new list by performing an opeartion on each item in an existing list

def my_list_comp():
    chars = []
    for ch in 'Danielle':
        chars.append(ch)
    print(chars)

            #(output exp) for (condition) in (iterable)
    chars2 = [ch for ch in 'Danielle']
    print(chars2)

    #get squar of each x in range 0-10
    squares = [x*x for x in range(11)]
    print(squares)

    #list of tuples
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    combine = [(x, y) for x in list1 for y in list2]
    print(combine)


    # list comprehension with optional predicate
    evens = [x for x in range(21) if x % 2 == 0]
    print(evens)

    # list comprehension with multiple optional predicate  (aka its an AND not a OR)
    numbers = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
    print(numbers)

    numbers2 = [x for x in range(21) if x % 2 == 0 or x % 5 == 0]  #( with OR)
    print(numbers2)

    # if else list comprehension
    obj = ['Even' if i % 2 ==0 else 'Odd' for i in range(10)]
    print(obj)

    # if else list comprehension
    obj = ['Even' if i % 2 ==0 else 'Odd' for i in range(10) if i % 5 ==0]
    print(obj)

    # flatten a list
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    flat_list = [num for row in matrix for num in row]
    print(flat_list)

    nums = [1,2,3,4]
    strs = ['a', 'b', 'c', 'd']
    # i want a (letter, num) pair for each letter in strs and each number in nums
    my_list = []
    for letter in strs:
        for num in nums:
            my_list.append((letter, num))
    print(my_list)

    my_list2 = [(letter, num) for letter in strs for num in nums]
    print(my_list2)

# my_list_comp()

def my_other_comp():
    # set comprehension
    nums = [1, 1, 2, 1, 3, 9, 4, 5, 5, 6, 7, 7, 8, 9, 10]
    my_set = set()
    for n in nums:
        my_set.add(n)
    print(my_set)

    my_set2 = {n for n in nums}
    print(my_set2)

    # dictionary comprehension
    names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
    secrets = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

    # I want a dict{'name': 'secret'} for each name, secret in zip(names, secrets)
    my_dict ={}
    for name, secret in zip(names, secrets):
        my_dict.update({name: secret})
        #my_dict[name] = secret
    print(my_dict)
    
    my_dict2 = {name: secret for name, secret in zip(names, secrets)}
    print(my_dict2)

    #unzip_names = [name for name, secret in my_dict2]
    #unzip_secrets = [secret for name, secret in my_dict2]
    #print(unzip_names)
    #print(unzip_secrets)
# my_other_comp()

#zip() func
# this is a good way to take two different sequences of data and pair them together

def my_zip():
    prices = [72.51, 9.27, 153.74, 30.23, 53.00]
    names = ['CAT', 'GE', 'MSFT', 'AA', 'IBM']

    # use for loop and zip() to pair the lists together
    for name, price in zip(names, prices):
        print(name, '=', price)

# my_zip()


# Generator Expressions
# I want to yield n*n for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen_var = gen_func(nums)
#print(next(my_gen_var))
#print(next(my_gen_var))

my_gen2 = (n*n for n in nums)
#for i in my_gen2:
#    print(i)


# enumerate

# iterates over different types of iterable objects and returns both the index and value for each item

def enum_names():
    names = ['Daniel', 'Joe', 'Jim','Travis']
    print(list(enumerate(names)))
    print(list(enumerate(names, start=4)))
    for name in enumerate(names, start=6):
        print(name)
    for count, item in enumerate(names, 100):
        print(f"Count: {count} \tItem: {item}")

def second_enum():
    my_str = 'Enumerate is Powerful'
    for idx, ch in enumerate(my_str):
        print(f'Index is {idx} anch Character is {ch}')

def enum_dict():
    #dictionary comprehnsion with enumerate
    names = ['Daniel', 'Joe', 'Jim','Travis']
    my_dict = {k: v for k, v in enumerate(names)}
    print(my_dict)
    my_dict_cond = {k: v for k, v in enumerate(names) if v.startswith('D')}
    print(my_dict_cond)
enum_dict()
