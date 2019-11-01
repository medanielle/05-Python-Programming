'''
Extra Looping Questions 
You’re not required to complete these, these are more of “challenge” questions. 
'''
'''
1. (Perfect number) A positive integer is called a perfect number if it is equal to the sum of all of its positive divisors, excluding it self. For example, 6 is the first perfect number, because 6 = 3 + 2 + 1. The next is 28 = 14 + 7 + 4 + 2 + 1.
Keep a counter of perfect numbers. How many perfect numbers exist before 10,000. Write a program to find these numbers.
'''
def getPerfectNum():
    for x in range(1, 10001):
        Sum = 0
        for i in range(1, x):
            if(x % i == 0):
                Sum = Sum + i
        if (Sum == x):
            print(f"{x} is a Perfect Number")

#getPerfectNum()
'''
2. (Game: rock, paper, scissors)
Programming Exercise 4.17 gives a program that plays the rock, paper, scissors game. Revise the program to let the user play continuously until either the user or the computer wins more than two times. 
'''
import random
def rockPaperScissors():
    #set 
    userWins = 0
    compWins = 0
    compWinning = ['rockscissors', 'scissorspaper', 'paperrock']
    userWinning = ['scissorsrock', 'paperscissors', 'rockpaper']
    tie = ['scissorsscissors', 'paperpaper', 'rockrock']
    
    while userWins < 3 and compWins < 3:
        computerNum = random.randint(1, 3)
        userString = input("Enter 'rock', 'paper' or scissors': ")
        print(f"Computers choice was {getNumToWords(computerNum)}")
        oneString = getNumToWords(computerNum) + userString
        if oneString in compWinning:
            print(f"The computer won!")
            compWins += 1
        elif oneString in userWinning:
            print(f"The user won!")
            userWins += 1

        elif oneString in tie:
            print(f"Its a TIE!")

def getNumToWords(num):
    words = 'wrong'
    if num ==1:
        words = "rock"
    elif num ==2:
        words = "paper"
    elif num == 3:
        words = "scissors"
    else:
        print(f"Error invalid entry, try again!")
    return words

rockPaperScissors()

'''
3. (Turtle: draw circles)
Write a program that draws 10 circles with centers (0, 0). Like below
'''
'''
4. (Turtle: display a multiplication table)
Write a program that displays a multiplication table
'''
'''
5. (Turtle: display a lattice)
Write a program that displays an 18-by-18 lattice
'''
'''
6. (Turtle: plot the sine and cosine functions) Write a program that plots the sine function in red and cosine in blue
'''
'''
7. (Turtle: chessboard) Write a program to draw a chessboard
'''