'''
File Exercises
'''
'''
1. File Display
Create a file containing a series of integers named numbers.txt. Write a program that displays all of the numbers in the file.
'''
def FileDisplay():
    # write integers into a file
    numbers = open('names.txt', 'r+')
    numbers.write('John\nJane\nEric\nDanielle\nSue\nJoe\n')
    contents = numbers.read()
    print(contents)
    numbers.close()

#FileDisplay()
'''
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only the first five lines of the file’s contents. If the file contains less than five lines, it should display the file’s entire contents.
'''
def getFileHeadDisplay():
    file_name = input('Enter a file name: ')
    f = open(file_name, 'r')
    line = f.readline()
    for x in range(5):
        print(line, end='')
        line = f.readline()
    f.close()

#getFileHeadDisplay()
'''
3. Line Numbers
Write a program that asks the user for the name of a file. The program should display the
contents of the file with each line preceded with a line number followed by a colon. The
line numbering should start at 1.
'''
def getLineNums():
    file_name = input('Enter a file name: ')
    f = open(file_name, 'r')
    line = f.readline()
    x = 1
    while line != '':
        print(f"{x}: {line}", end='')
        line = f.readline()
        x += 1
    f.close()

#getLineNums()
'''
4. Item Counter
Assume that a file containing a series of names (as strings) is named names.txt and exists
on the computer’s disk. Write a program that displays the number of names that are stored
in the file. (Hint: Open the file and read every string stored in it. Use a variable to keep a
count of the number of items that are read from the file.)
'''
def getItemCounter():
    #file_name = input('Enter a file name: ')
    f = open('names.txt', 'r')
    line = f.readline()
    x = 1
    myStr = ''
    while line != '':
        x += 1
        myStr += line.replace('\n', ' ')
        line = f.readline()
    print(myStr,'\nThe number of names: ', x)
    f.close()

#getItemCounter()
'''
5. Sum of Numbers
Assume that a file containing a series of integers is named numbers.txt and exists on the computer’s disk. Write a program
that reads all of the numbers stored in the file and calculates their total.
'''
def getSumOfNums():
    #file_name = input('Enter a file name: ')
    f = open('numbers.txt', 'r')
    line = f.readline()
    total = 0
    myStr = ''
    while line != '':
        total += int(line)
        myStr += line.replace('\n', ' ')
        line = f.readline()
    print(myStr, '\nThe sum of numbers.txt: ', total)
    f.close()

#getSumOfNums()

'''
6. Average of Numbers
Assume that a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in
the file.
'''
def getAvgOfNums():
    #file_name = input('Enter a file name: ')
    f = open('numbers.txt', 'r')
    line = f.readline()
    total = 0
    myStr = ''
    count = 0
    while line != '':
        total += int(line)
        myStr += line.replace('\n', ' ')
        count+=1
        line = f.readline()
    print(myStr, '\nThe Average of numbers.txt: ', (total/count))
    f.close()

#getAvgOfNums()
'''
7. Random Number File Writer
Write a program that writes a series of random numbers to a file. Each random number
should be in the range of 1 through 100. The application should let the user specify how
many random numbers the file will hold.
'''
import random
def getRandomNums():
    amount = int(input('Enter a number of random integers: '))
    f = open('random.txt', 'w')
    for x in range(1, amount+1):
        new_ran = str(random.randint(1, 100))
        f.write(f'{new_ran}\n')
    f.close()

#getRandomNums()

'''
8. Random Number File Reader
This exercise assumes you have completed Programming Exercise 7, Random Number File
Writer. Write another program that reads the random numbers from the file, display the
numbers, and then display the following data:
• The total of the numbers
• The number of random numbers read from the file
'''
def getRandomReader():
    #file_name = input('Enter a file name: ')
    f = open('random.txt', 'r')
    line = f.readline()
    total = 0
    myStr = ''
    count = 0
    while line != '':
        total += int(line)
        myStr += line.replace('\n', ' ')
        count+=1
        line = f.readline()
    print(f'{myStr} \nThe total of all random #s: {total}\nThen number of random #s: {count}')
    f.close()

#getRandomReader()

'''
9. Exception Handing
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
• It should handle any IOError exceptions that are raised when the file is opened and data
is read from it.
'''
def getAvgNumsError():
    try:
        file_name = input('Enter a file name: ')
        f = open(file_name, 'r')
        line = f.readline()
        total = 0
        myStr = ''
        count = 0
        while line != '':
            total += int(line)
            myStr += line.replace('\n', ' ')
            count+=1
            line = f.readline()
        print(f'{myStr}\nThe Average of {file_name}: {(total/count)}')
        f.close()
    except IOError:
        print(f'An error occured trying to read the {file_name} file:')

#getAvgNumsError()
'''
10. Golf Scores
The Springfork Amateur Golf Club has a tournament every weekend. The club president
has asked you to write two programs:
    1. A program that will read each player’s name and golf score as keyboard input, and then
save these as records in a file named golf.txt. (Each record will have a field for the
player’s name and a field for the player’s score.)
    2. A program that reads the records from the golf.txt file and displays them.
'''
def getGolfScores():
    #open file and set up sentinel
    f = open('golf.txt', 'w')
    again = 'y'
    
    #loop until user says to stop
    while again.lower() == 'y':
        #gather name and score from user
        name = input("\nEnter golfer's name: ")
        score = input(f"Enter {name}'s score: ")
        #write into the golf.txt doc
        f.write(f'{name},{score}\n')
        again = input("Do you want to enter another name (y/n)? ")
    print(f'\nThanks for the Data!')
    #ALWAYS CLOSE
    f.close
    
    
def readGolfScores():
    #open file and read first line
    f = open('golf.txt', 'r')
    line = f.readline()
    print(f"\n\nGolfer's Name \t Score")
    
    #while loop to read and display each line
    while line != '':
        name, score = line.split(',')
        print(f"  {name}\t\t  {score}", end='') 
        line = f.readline()
    f.close()

getGolfScores()
readGolfScores()