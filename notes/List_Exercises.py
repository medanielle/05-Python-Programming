#List and Tuple Exercises
'''
 1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. The
amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result.
'''
def getSales():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    sales = []
    for x in range(7):
        sales.append(int(input(f'Enter the sales for {days[x]}: ')))
    return sales

def getTotal(p_sales):
    total = 0
    for item in p_sales:
        total += item
    print(f"\nYour total sales for the week are ${total:.2f}")

#getTotal(getSales())
'''
 2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element. Then write another loop that displays the contents of the list.
'''
import random
def getLottery():
    lottery_nums = []
    for x in range(7):
        lottery_nums.append(random.randint(0, 9))
    return lottery_nums

def getPrint(p_num):
    print('The lotery numbers are', end= ' ')
    for item in p_num:
        print(item, end=' ')

#getPrint(getLottery())
'''
 3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year, the average monthly
rainfall, and the months with the highest and lowest amounts.
'''
MONTHS = 12
def getRain():
    rainfall = []
    for x in range(MONTHS):
        rainfall.append(float(input(f'Enter the rainfall for month #{x+1}: ')))
    return rainfall

def getRainCalc(p_rain):
    total = 0
    for item in p_rain:
        total += item
    print(f"\nYour total rain for the year is ${total}")
    print(f"Your average rain is {total/MONTHS}")
    print(f"Your max rain month amount is {max(p_rain)}")
    print(f"Your min rain month amount is {min(p_rain)}")

#getRainCalc(getRain())

'''
 4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
'''
NUMBERS = 20
def getNumbers():
    num_list = []
    for x in range(NUMBERS):
        num_list.append(int(input(f'Enter number #{x+1}: ')))
    return num_list

def getNumCalc(p_num_list):
    total = 0
    for item in p_num_list:
        total += item
    print(f"\nYour lowest number entered is {min(p_num_list)}")
    print(f"Your highest number entered is {max(p_num_list)}")
    print(f"The total of all numbers entered is {total}")
    print(f"Your average number entered is {total/NUMBERS}")

#getNumCalc(getNumbers()) 

'''
 6. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here are the correct answers:

1. B 	6. A 	11. B 	16. C
2. D 	7. B 	12. C 	17. C
3. A 	8. A 	13. D 	18. B
4. A 	9. C 	14. A 	19. D
5. C 	10. D 	15. D 	20. A

Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.
'''
def getScore(p_answers):
    correct = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', \
                'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', \
                'C', 'B', 'D','A']
    index = 0
    correct_num = 0
    wrong_num = 0
    wrong = []
    for x in p_answers:
        if x == correct[index]:
            correct_num += 1
        else:
            wrong_num += 1
            wrong.append(str(index+1))
        index +=1
    return correct_num, wrong_num, wrong

def getAnswers():
    infile = open('answers2.txt', 'r')
    answers_read_in = infile.readlines()
    index = 0
    while index < len(answers_read_in):
        answers_read_in[index] = answers_read_in[index].rstrip('\n')
        index += 1
    infile.close()
    return(answers_read_in)

def getResults():
    score, bad, wrong_list = getScore(getAnswers())
    if score >= 15:
        print('You Passed!\n')
    else:
        print('You Failed!\n')
    print(f'Score = {score}\nWrong = {bad}\nList of Wrong:{wrong_list}')

#getResults()
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
ROWS = 4
COLUMNS = 4

def getRandMatrix():
    #intialize variables
    values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row_total_list = [0, 0, 0, 0]
    col_total_list = [0, 0, 0, 0]

    #Create random matric AND create a col/row total list 
    for r in range(ROWS):
        #intialize row acculumator
        row_total = 0
        for c in range(COLUMNS):
            values[r][c] = random.randint(0, 1)
            #keep running tally of row total
            row_total += values[r][c]
            #keep running tally of col total
            col_total_list[c] = col_total_list[c] + values[r][c]
        #add each row to list of totals
        row_total_list[r] = int(row_total)
    #create list of column totals  

    
    #print out pretty matrix
    print('The matrix is')
    for item in values:
        print(item)

    ##FOR TESTING
    print(f'Col List: {col_total_list}\nRow List: {row_total_list}')

    #display largest row & decision on which index is largest
    r_largest =  [row_total_list.index(max(row_total_list))]
    index = 0
    count = 0
    for x in row_total_list:        
        if x == max(row_total_list):
            count += 1
            if count >= 2:
                r_largest.append(index)
        index += 1
    print(f'Largest Row: {r_largest}')

    #display largest col & decision on which index is largest
    c_largest =  [col_total_list.index(max(col_total_list))]
    index = 0
    count = 0
    for x in col_total_list:        
        if x == max(col_total_list):
            count += 1
            if count >= 2:
                c_largest.append(index)
        index += 1
    print(f'Largest Col: {c_largest}')

#getRandMatrix()

'''
def getMatrixPrint(p_matrix):
    print('The matrix is')
    for item in p_matrix:
        print(item)

def getMostRows(p_values):
    rows_total = [0, 0, 0, 0]
    r_index = 0
    c_index = 0
    print('The matrix is')
    for item in p_values:
        print(item)
    for row in p_values:
        total = 0
        #print(row)
        for col in p_values:
            total += int(p_values[r_index][c_index])
            print(total)
            c_index += 1
            #total += p_values[row][col]
        #rows_total[index] = total
        #print(rows_total)
        r_index += 1
    print(rows_total)

#getMatrixPrint(getRandMatrix())
'''
'''
8. (Game: play a tic-tac-toe game) 
In a game of tic-tac-toe, two players take turns marking an available cell in a grid with their 
respective tokens (either X or O). When one player has placed three tokens in a horizontal, vertical, or diagonal
row on the grid, the game is over and that player has won. A draw (no winner)
occurs when all the cells in the grid have been filled with tokens and neither player
has achieved a win. Create a program for playing tic-tac-toe.
The program prompts two players to alternately enter an X token and an O
token. Whenever a token is entered, the program redisplays the board on the
console and determines the status of the game (win, draw, or continue).
'''

import re
def getTicTacToe():
    grid = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
    winner = False

    while winner == False:
        grid = getInput('1', 'X', grid)
        winner = getWinner(grid, '1')
        if winner == True:
            continue
        grid = getInput('2', 'O', grid)
        winner = getWinner(grid, '2')

def getInput(p_player, p_sign, p_grid):
    
    for item in p_grid:
        print(item)
    row, col = int(input(f'Player {p_player} Row: ')), int(input(f'Player {p_player} Column: '))
    while row > 2 or row < 0 or col > 2 or col < 0:
        print('Try Again! Number must be (0-2)')
        row, col = int(input(f'Player {p_player} Row (0-2): ')), int(input(f'Player {p_player} Column (0-2): '))
    while p_grid[row][col] != 'e':
        print('Try Again!')
        row, col = int(input(f'Player {p_player} Row (0-2): ')), int(input(f'Player {p_player} Column (0-2): '))
    p_grid[row][col] = p_sign
    print(f'player {p_player} is {p_sign}\nGrid value is {p_grid[row][col]}')
    return p_grid
    
def getWinner(p_grid, p_player):
    answer = ''
    for item in p_grid:
        answer += ''.join(item)
    #diagonal
    if re.search('[XO]...[XO]...[XO]', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #diagonal2
    if re.search('..[XO].[XO].[XO]..', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #row1
    elif re.search('[XO][XO][XO]......', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #row2
    elif re.search('...[XO][XO][XO]...', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #row3
    elif re.search('......[XO][XO][XO]', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #col1
    elif re.search('[XO]..[XO]..[XO]..', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #col2
    elif re.search('.[XO]..[XO]..[XO].', answer):
        print(f'Player {p_player} wins!')
        winner = True
    #col3
    elif re.search('..[XO]..[XO]..[XO]', answer):
        print(f'Player {p_player} wins!')
        winner = True
    else:
        winner = False
    return winner

getTicTacToe()