'''
Repetition Structures
1. Bug Collector
A bug collector collects bugs every day for seven days. Write a program that keeps a running total of 
the number of bugs collected during the seven days. The loop should ask for the number of bugs collected 
for each day, and when the loop is finished, the program should display the total number of bugs collected.
'''
def getBugsCollected():
    count = 0
    total = 0
    while count < 7:
        total += int(input('Enter number of bugs collected today :'))
        count += 1
    print(f'\nYou entered {total} bugs this week!')
    
#getBugsCollected()
'''
2. Calories Burned
Running on a particular treadmill you burn 3.9 calories per minute. Write a program
that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30
minutes.
'''
def getBurnedCals():
    minutes = 10
    while minutes <= 30:
        print(f'\nYou burned {(minutes*3.9)} calories in {minutes} minutes!')
        minutes += 5

#getBurnedCals()
'''
3. Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for a
month. A loop should then prompt the user to enter each of his or her expenses for the
month, and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.
'''
def getBudgetAnalysis():
    #get budget goal and set expenses to something other than 0
    userBudget = float(input("Enter your budget for the month:"))
    expenses = 1
    #start while loop to ask user for expesnse until done
    while expenses != 0:
        expenses = float(input('\nEnter expenses (Use 0 to stop): '))
        userBudget -= expenses
    #display data to custoer (decide if over/under budget)
    if userBudget >0:
        print(f'You are underbudget! ${userBudget:.2f} left!')
    else:
        print(f'You are overbudget! ${userBudget:.2f} in the hole!')

#getBudgetAnalysis()
'''
4. Distance Traveled
The distance a vehicle travels can be calculated as follows:
distance = speed* time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120
miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) and
the number of hours it has traveled. It should then use a loop to display the distance the
vehicle has traveled for each hour of that time period. 
'''
def getDistTravel():
    speed = int(input('the speed of a vehicle (in miles per hour): \n'))
    time = int(input('the number of hours it has traveled: \n'))
    count = 1
    while count <= time:
        print(f'Vehicle Distance after {count} hour(s): {(speed*count)}')
        count += 1
    
#getDistTravel()
'''
5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over a period 
of years. The program should first ask for the number of years. The outer loop will iterate once for 
each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop 
will ask the user for the inches of rainfall for that month. After all iterations,the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

def getAvgRain():
    years = int(input('Enter number of years: '))
    totalRain = 0
    months = years*12
    while years > 0:
        for x in range(12):
            totalRain += int(input(f'Enter rainfall for month {x+1}: '))
        years -=1
    print(f'\nNumber of months: {months}\nTotal Rainfall (in inches): {totalRain}' 
            f'\nAverage rain per month: {totalRain/months}')

#getAvgRain()
'''
6. Celsius to Fahrenheit Table
Write a program that displays a table of the Celsius temperatures 0 through 20 and their
Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is
F = (9/5)C + 32
where F is the Fahrenheit temperature and 
C is the Celsius temperature. 
Your program must use a loop to display the table.
'''

def getCelToFah():
    print(f'Celcius \t Fahrenheit\n ------------------------------ \n')
    for x in range(20):
        print(f'{x+1:4d} \t\t   {(9/5)*(x+1)+32:.2f}')

#getCelToFah()
'''
7. Pennies for Pay
Write a program that calculates the amount of money a person would earn over a period
of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number
of pennies.
'''

def pennyADay():
    days = int(input('Enter number of days: '))
    salary = .01
    totalMoney = 0
    print(f'  Day \t Salary \n----------------- \n')
    for x in range(days):
        print(f'   {x+1:2d} \t  ${salary:.2f}')
        totalMoney += salary
        salary *= 2
    print(f'\nTotal Salary = ${totalMoney:.2f}')

pennyADay()
'''
8. Sum of Numbers
Write a program with a loop that asks the user to enter a series of positive numbers. The
user should enter a negative number to signal the end of the series. After all the positive
numbers have been entered, the program should display their sum.
'''

def getPosTotal():
    num = 0
    total = 0
    while num >=0:
        total += num
        num = int(input('Enter positive whole #s to sum (negative #s to exit): '))
    print(f'Total = {total}')

#getPosTotal()
'''
9. Write a program that uses nested loops to draw 
this pattern:
*******
******
*****
****
***
**
*
'''

def createTriangle():
    num = 7
    for x in range(7):
        for x in range(num):
            print ('*', end='')
        print()
        num -= 1

#createTriangle()
'''
10. Write a program that uses nested loops to draw
this pattern:
##
# #
#  #
#   #
#    #
#     #
(add a space in between the symbol every row after 
the first row
'''

def pattern_draw():
    spaces = 0
    while spaces < 6:
        pattern = '#'
        for x in range(spaces):
            pattern += ' '
        pattern += "#"
        spaces += 1
        print(f'{pattern}')

pattern_draw()
