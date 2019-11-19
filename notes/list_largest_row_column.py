"""

(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3

"""

import random

n = 4
def main():
    matrix = []
    # This nested loop fills out the matrix with random 0s or 1s
    for i in range(n):
        matrix.append([])
        for j in range(n):
            # import pdb; pdb.set_trace()                         # add for pdb breakpoint
            matrix[i].append(random.randint(0, 1))
            print(matrix[i][j], end = " ")

        print()

    # Check rows
    rowSum = sum(matrix[0])
    rowList = [0]
    for i in range(1, n):
        if rowSum < sum(matrix[i]):
            rowSum = sum(matrix[i])
            rowList = [i]
        elif rowSum == sum(matrix[i]):
            rowList.append(i)
            
    print("The largest row index: ", end = "")
    for i in range(len(rowList) - 1):
        print(rowList[i], end = ", ")
    print(rowList[len(rowList) - 1])

    # Check columns
    columnSum = sumColumn(matrix, 0)
    columnList = [0]
    for j in range(1, n):
        if columnSum < sumColumn(matrix, j):
            columnSum = sumColumn(matrix, j)
            columnList = [j]
        elif columnSum == sumColumn(matrix, j):
            columnList.append(j)
            
    print("The largest column index: ", end = "")
    for i in range(len(columnList) - 1):
        print(columnList[i], end = ", ")
    print(columnList[len(columnList) - 1])

# This function sums up the column  
def sumColumn(m, j):
    sum = 0
    for i in range(n):
        sum += m[i][j]
    return sum

main()

# Debug with pdb

# C:\Users\student\Documents\05-Python-Programming\notes>python -m pdb list_largest_row_column.py

# -> """
#(Pdb) h     => for help
# add break point (line 23)

# cmds => step, break, next, list
'''
-> matrix[i].append(random.randint(0, 1))
(Pdb) list
 20         # This nested loop fills out the matrix with random 0s or 1s
 21         for i in range(n):
 22             matrix.append([])
 23             for j in range(n):
 24                 import pdb; pdb.set_trace()                         # add for pdb breakpoint
 25  ->             matrix[i].append(random.randint(0, 1))
 26                 print(matrix[i][j], end = " ")
 27     
 28             print()
 29
 30         # Check rows
(Pdb)
'''
# list 10 (goes to line 10 and prints code)
# h list
'''
(Pdb) h list
l(ist) [first [,last] | .]

        List source code for the current file.  Without arguments,
        list 11 lines around the current line or continue the previous
        listing.  With . as argument, list 11 lines around the current
        line.  With one argument, list 11 lines starting at that line.
        With two arguments, list the given range; if the second
        argument is less than the first, it is a count.

        The current line in the current frame is indicated by "->".
        If an exception is being debugged, the line where the
        exception was originally raised or propagated is indicated by
        ">>", if it differs from the current line.
'''
# (Pdb) next   (goes into next step of function)
# # # # # # # # c:\users\student\documents\05-python-programming\notes\list_largest_row_column.py(26)main()
#-> print(matrix[i][j], end = " ")
#(Pdb) l    
# 21         for i in range(n):
# 22             matrix.append([])
# 23             for j in range(n):
# 24                 import pdb; pdb.set_trace()                         # add for pdb breakpoint
# 25                 matrix[i].append(random.randint(0, 1))
# 26  ->             print(matrix[i][j], end = " ")
# 27
# 28             print()
# 29
# 30         # Check rows
# 31         rowSum = sum(matrix[0])
#(Pdb)

# (Pdb) continue (goes until next break point)
# (Pdb) p <variable> (prints values?)


# VSCode click to the left of number lines. make red button if you want break point 

# VSCode => Ctrl + Shift + D => bring up debug window

# VSCode => put breakpooint on the loop (if/while to see variables after each run thru)

"""
Continue/Pause (F5)
Step Over (F10)
Step Into (F11)
Step Out (Shift + F11)
Restart (Ctrl + Shift + F5)
Stop (Shift + F5)
"""
