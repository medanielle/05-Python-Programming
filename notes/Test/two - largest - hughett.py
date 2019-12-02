from random import randint, uniform, random
"""
n = 4
def Curran():
    matrix = []
    # This nested loop fills out the matrix with random 0s or 1s
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.random(0, 20))
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
"""
"""
2.
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:
    
    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a 
        two-dimensional list and displays the location of the largest element in the list. 
    
    Here is a sample run(You don't have to mimic this, this is just a guide):

        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)

        """

def create_matrix():
    # intialize variables the blank matrix
    matrix = []

    # get input from user for number of rows and columns
    rows = int(input('Enter the number of rows in the list: '))
    cols = int(input('Enter the number of cols in the list: '))

    # This nested loop fills out the matrix
    # loop through each row
    for i in range(rows):
        # create new list in next element
        matrix.append([])
        # loops through each column to that row
        for j in range(cols):
            # get input from user
            num = int(input(f'Enter integer for {i+1, j+1}: '))
            #append to the current elements list
            matrix[i].append(num)
    return matrix

def largest_element(p_matrix):
    # intialize row variable as accumulator
    row = 0
    # intialize large_num to 0 to compare with each new number
    large_num = 0
    # loop through each row in the matrix
    for listy in p_matrix:
        # row starts at 1(for the first row)
        row += 1
        print(listy)
        # if the largest number in this row is larger than our current highest number then
        if max(listy) > large_num:
            # reset the largest number
            large_num = max(listy)
            # track the elements place (row, column) / starting at 1
            element_list = [row, listy.index(large_num) + 1]
    return element_list

def main():
    # set a variable and call function to create the two dimensional list
    user_matrix = create_matrix()
    # set variable for coordinates to the largest element (found first) no duplicates
    element = largest_element(user_matrix)
    # display
    print(f"The location of the largest element is at ({element[0]}, {element[1]})")

main()