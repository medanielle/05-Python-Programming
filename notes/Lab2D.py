"""Answer:

my_str = input("Please enter a string: ")
str_reversed_upper = my_str[::-1].upper()
print ("string uppercase & reversed", str_reversed_upper)

More functionality
"""
my_str = input("Please enter a string: ")
str_reversed = my_str[::-1]
print("string reversed: ", str_reversed)
str_upper = str_reversed.upper()
print ("string uppercase:", str_upper)
str_lower = str_reversed.lower()
print ("string lower case:", str_lower)

"""
x = input()
count = len(x) -1
rev_str = ''
while count >= 0:
    rev_str +=x[count].upper()
    count -= 1

print("Your string was")
print("reversed and cap")

"""

'''
print(''.join(reversed(input("Enter string: "))).upper())
'''

'''
print(''.join(reversed(input("Enter string: "))).upper())
'''
