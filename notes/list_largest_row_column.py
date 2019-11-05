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
def Curran():
    matrix = []
    # This nested loop fills out the matrix with random 0s or 1s
    for i in range(n):
        matrix.append([])
        for j in range(n):
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

Curran()


def Howard():
    import random
    ​
    # initialize the 2d list for the matrix
    matrix = [[],[],[],[]]
    # initalize lists for the highest rows and columns
    highestRow = [0]
    highestCol = []
    # for loop enumerating over the rows of matrix
    for index, row in enumerate(matrix):
        # initialize accumulator
        total = 0
        # for loop for 4 entries into each matrix row
        for _ in range(4):
            # generate a random number and add it to the matrix and to the accumulator
            randNum = random.randint(0,1)
            row.append(randNum)
            total += randNum
        # print the matrices
        print(row)
        # if not the first row
        if index != 0:
            # check if this row is bigger and replace the list if so
            if total > matrix[highestRow[0]].count(1):
                highestRow = [index]
            # otherwise, check if row is the same size and add it to list
            elif total == matrix[highestRow[0]].count(1):
                highestRow.append(index)
    # print highest row results
    print("Highest row(s):", highestRow)
    # initialize a list of accumulators for columns
    total = [0,0,0,0]
    # double range loop to get the matching indices for rows and columns
    for index in range(4):
        for index2 in range(4):
            # reverse the usage of indices to check columns instead of rows
            # and add to appropriate accumulator
            total[index] += matrix[index2][index]
    # for loop for the accumulators to check which ones are the highest
    for i in range(total.count(max(total))):
        highestCol.append(total.index(max(total)) + i)
        total.remove(max(total))
    # print results of highest column check
    print("Highest column(s):", highestCol)

Howard()


def camaratta():
        '''
    7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
    a matrix, prints the matrix, and finds the rows and columns with the most
    1s. Here is a sample run of the program:
    0011
    0011
    1101
    1010
    The largest row index: 2
    The largest column index: 2, 3
    '''
    import random
    ​
    # prints out extra information at the end
    DEBUG = False
    ​
    # declartions
    # HARD MODE: randomize the columns and rows of the matrix
    MAX_ROWS = random.randint(2,10)
    MAX_COLS = random.randint(2,10)
    ​
    # generate the matrix
    the_matrix = []
    for row in range(MAX_ROWS):
        the_matrix.append([random.randint(0,1) for i in range(MAX_COLS)])
    ​
    # print the matrix
    for row in the_matrix:
        for col in row:
            print(col, end='')
        print()
    ​
    # largest row in the matrix
    row_sums = []
    for row in the_matrix:
        row_sums.append(sum(row))
    ​
    #  flatten the matrix
    flat_matrix = []
    for row in the_matrix:
        for col in row:
            flat_matrix.append(col)
    ​
    # step through the flattened matrix
    col_sums = []
    for row in range(MAX_COLS):
        col_sums.append(sum(flat_matrix[row::MAX_COLS]))
    ​
    # find a largest row and add it's index to a list
    row_max_indicies = []
    for index, value in enumerate(row_sums):
        if value == max(row_sums):
            row_max_indicies.append(index)
    print(f"The largest row index: {row_max_indicies}")
    ​
    # find a largest column and add it's index to a list
    col_max_indicies = []
    for index, value in enumerate(col_sums):
        if value == max(col_sums):
            col_max_indicies.append(index)
    print(f"The largest column index: {col_max_indicies}")
    ​
    if DEBUG:
        print("matrix", the_matrix)
        print("flat_matrix", flat_matrix)
        print("col_sums", col_sums)
        print("row_sums", row_sums)

camaratta

def chunn():
    '''
 7. (Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3
​'''
​
    def largest_rows_columns():
        # building the matrix
        # initialize the list for the matrix to work in
        matrix = []
        # grab a random integer between 2 and 10, inclusive, to determine the size of the matrix
        SIZE = randint(2,10)
        # iterate through a range up to the rng size variable
        for build_row in range(SIZE):
            # set an empty string to begin building the binary pattern
            m_row = []
            # iterate through a range of the matrix size constant to build the columns entry
            for build_columns in range(SIZE):
                # append a random integer (0, 1) to the row pattern
                m_row.append(randint(0, 1))
            # append the built row to the matrix
            matrix.append(m_row)
        
        # for better formatting add a blank print statement
        print('')
        # Iterate through each row to print the matrix
        for print_row in matrix:
            # Initialize a variable to represent the matrix in string format
            row_str_rep = ''
            # iterate for each element in the row
            for print_char in print_row:
                # add the string value of the element to the string
                row_str_rep += str(print_char)
            # display the rows, one row per line
            print(row_str_rep)
    ​
        # reading the matrix
        # initialize a new list to store the results of ones in each row
        calc_rows = []
        # initialize a new list/accumalator to store the results of ones in each column
        calc_columns = [0] * SIZE
    ​
        # iterate over each row in the matrix
        for row in matrix:
            # sum the row and append it to calc_rows list
            calc_rows.append(sum(row))
            # Iterate ovet each element in the row to get the column count
            for index in range(len(row)):
                # if element in index == 1 ; do nothing if element != 1
                if row[index] == 1:
                    # increment the column counter
                    calc_columns[index] += 1
    ​
        # assign the max of calcs rows to a variable
        highest_row = max(calc_rows)
        # Check if only one occurance of max value in row
        if calc_rows.count(highest_row) > 1:
            # initial a counter to keep track of removed indexes
            removed_count = 0
            # initialize a list to store multiple indexes
            max_rows = []
            # continuously pull and del indexes until the count of max value == 0
            while calc_rows.count(highest_row) > 0:
                # assign the first index of the max of calc_rows to a variable
                max_val_index = calc_rows.index(highest_row)
                # append the first max value index to the list + the counter of removed indexes
                max_rows.append(str(max_val_index + removed_count))
                # del the index of the first max value
                del(calc_rows[max_val_index])
                # increment counter of removed indexes
                removed_count += 1
            # convert the list to a string for printing
            string_rep_rows = ', '.join(max_rows)
            # print the rows with the greatest value
            print(f'\nlargest row indexes: {string_rep_rows}')
        # if only 1 instance
        else:
            # Display the largest row
            print(f'\nlargest row index: {calc_rows.index(highest_row)}')
        # assign the max of calcs columns to a variable
        highest_column = max(calc_columns)
        # check if only 1 occurance of max value in column
        if calc_columns.count(highest_column) > 1:
            # initial a counter to keep track of removed indexes
            removed_count = 0
            # initialize a list to store multiple indexes
            max_columns = []
            # continuously pull and del indexes until the count of max value == 0
            while calc_columns.count(highest_column) > 0:
                # assign the first index of the max of calc_rows to a variable
                max_val_index = calc_columns.index(highest_column)
                # append the first max value index to the list + the counter of removed indexes
                max_columns.append(str(max_val_index + removed_count))
                # del the index of the first max value
                del(calc_columns[max_val_index])
                # increment counter of removed indexes
                removed_count += 1
            # convert the list to a string for printing
            string_rep_columns = ', '.join(max_columns)
            # print the columns with the greatest value
            print(f'largest column indexes: {string_rep_columns}')
        # if only 1 instance
        else:
            # Display the largest column
            print(f'largest column index: {calc_columns.index(highest_column)}')
    ​
    largest_rows_columns()
chunn()
