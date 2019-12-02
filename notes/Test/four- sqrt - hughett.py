"""
4. 
    (The sqrt function) Write a program that prints the following table
    using your knowledge of loops and the sqrt function in the math module.
    Make sure your table is neat by using print formatting methods we've learned. 

        Number  Square Root
        0       0.0000
        1       1.0000
        2       1.4142
        ...
        18      4.2426
        20      4.4721
"""

from math import sqrt

def main():
    # display the column names
    print('\tNumbers  Square Root')

    # iterate through a range of number starting at 0 and going through the # 20
    for i in range(21):
        # set this variable  as the square root of the index
        my_sqrt = sqrt(i)
        # print this index and the square root of that index
        print(f'\t{i} \t {my_sqrt:.4f}')

# call the function
# main()

ranger = [x for x in range(21)]
print(ranger)