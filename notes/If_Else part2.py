'''
1. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 
through 10. The program should display the Roman numeral version of that number. 
If the number is outside the range of 1 through 10, the program should display 
an error message. 
'''
def roman():
    # set dictionary
    roman = {1: 'I', 2: 'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IV', 10:'X'}
    # ask for num from user
    num = int(input("enter number (1-10): "))

    if (num < 1) or (num > 10):
        ## print error
        print("You entered a bad number!")
    else:
        ## print conversion
        print(f'{num} is {roman[num]} in Roman Numerals!')
    return

#roman()
'''
2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same. 
'''
def AreaRectangle():
    firstArea = int(input("Enter the length of the first rectangle: ")) \
        *int(input("Enter the width of the first rectangle: "))
    secondArea = int(input("Enter the length of the second rectangle: ")) \
        *int(input("Enter the width of the second rectangle: "))

    if firstArea > secondArea:
        print(f'\nThe first rectangle is larger!\nFirst = {firstArea}\tSecond = {secondArea}')
    elif secondArea > firstArea:
        print(f'\nThe second rectangle is larger!\nFirst = {firstArea}\tSecond = {secondArea}')
    else:
        print(f'\nThey are the same!\nFirst = {firstArea}\tSecond = {secondArea}')
    return

#AreaRectangle()
'''
3. Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the
amount of mass of an object in kilograms, you can calculate its weight in newtons with the
following formula:
weight =mass * 9.8 
Write a program that asks the user to enter an object’s mass, and then calculates its weight.
If the object weighs more than 1,000 newtons, display a message indicating that it is too
heavy. If the object weighs less than 10 newtons, display a message indicating that it is too
light. 
'''
def getWeightFromMass():
    mass= input("Enter a mass(in kgs): ")
    weight = float(mass) * 9.8
    if weight >1000:
        print(f'\nToo High!!\nYour mass of {mass} kgs is {weight:.0f} newtons.')
    elif weight <10:
        print(f'\nToo Low!!\nYour mass of {mass} kgs is {weight:.0f} newtons.')
    else:
        print(f'\nYour mass of {mass} kgs is {weight:.0f} newtons.')

#getWeightFromMass()
'''
4. Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. 
The program should then determine whether the month times the day equals the year. 
If so, it should display a message saying the date is magic. Otherwise, it should display a message 
saying the date is not magic. 
'''
def getMagicDate():
    month = int(input("Enter a month (in numeric form): "))
    day = int(input("Enter a day (in numeric form): "))
    year = int(input("Enter a two digit year: "))
    mtimesd = month * day
    if mtimesd == year:
        print(f"\n{month}/{day}/{year} is a MAGIC DATE!!!")
    else:
        print(f"\n{month}/{day}/{year} is a not a magic date!")

#getMagicDate()
'''
5. Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be
made by mixing other colors. When you mix two primary colors, you get a secondary color,
as shown here: 
    When you mix red and blue, you get purple.
    When you mix red and yellow, you get orange.
    When you mix blue and yellow, you get green. 
Design a program that prompts the user to enter the names of two primary colors to mix.
If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. 
Otherwise, the program should display the name of the secondarycolor that results. 
'''
def getSecondaryColor():
    my_flag = False
    options = ['red','blue','yellow']

    while my_flag == False:
        firstColor = input("Enter first Primary Color: ")
        secondColor = input("Enter second Primary Color: ")
        if firstColor in options and secondColor in options:
            my_flag = True
            print(f"{firstColor} and {secondColor} make {getSecond(firstColor,secondColor)}")
        else:
            print("Error! Only enter primary colors, Try Again!")

def getSecond(fColor, sColor):
    if fColor == sColor:
        finalColor = fColor
    elif fColor == 'red' or sColor =='red':
        if fColor == 'yellow' or sColor =='yellow':
            finalColor = 'orange'
        if fColor == 'blue' or sColor =='blue':
            finalColor = 'purple'
    elif fColor == 'blue' or sColor =='blue':
        if fColor == 'yellow' or sColor =='yellow':
            finalColor == 'green'
    return finalColor

#getSecondaryColor()
'''
6. Change for a Dollar Game
Create a change-counting game that gets the user to enter the number of coins required to make
exactly one dollar. 

The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. 

If the total value of the coins entered is equal to one dollar, 
the program should congratulate the user for winning the game. 

Otherwise, the program should display a message indicating whether the amount entered was
more than or less than one dollar.
'''
def getDollarChange():
    #get the info from customer and intialize total
    change = {.01: int(input("Enter number of pennies: ")), .05: int(input("Enter number of nickels: ")), 
            .1: int(input("Enter number of dimes: ")), .25: int(input("Enter number of quarters: "))}
    total = 0.0
    #add up the change
    for x in change.keys():
        total += (x*change[x])
    #check if the total is $1, or if they lose
    if total == 1:
        print(f'\nYou WIN! your total change was {total:.2f}')
    else:
        print(f'\nYou LOSE! your total change was {total:.2f}')
    return

#getDollarChange()

'''
7. Book Club PointsSerendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 5 points.
• If a customer purchases 2 books, he or she earns 15d points.
• If a customer purchases 3 books, he or she earns 30 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has purchased this month 
and displays the number of points awarded. 

8. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table: 
Quantity Discount
10–19       20%
20–49       30%
50–99       40%
100 or more 50% 
Write a program that asks the user to enter the number of packages purchased. The program should 
then display the amountof the discount (if any) and the total amount of thepurchase after the discount. 

9. Shipping Charges
The Fast Freight Shipping Company charges the following rates: 
Weight of Package                               Rate per Pound
2 pounds or less                                $1.10
Over 2 pounds but not more than 6 pounds        $2.20
Over 6 pounds but not more than 10 pounds       $3.70
Over 10 pounds                                  $3.80
Write a program that asks the user to enter the weight of a package and then displays the
shipping charges. 
10. Body Mass Index Program Enhancement
In programming Exercise #6 in Chapter 3 you were asked to write a program that calculates a 
person’s body mass index (BMI). Recall from that exercise that the BMI is often used
to determine whether a person is overweight or underweight for their height. A person’s
BMI is calculated with the formula
BMI =weight * 703 / height^2
where weight is measured in pounds and height is measured in inches. Enhance the program 
so it displays a message indicating whether the person has optimal weight, is
underweight, or is overweight. A person’s weight is considered to be optimal if his or
her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered
to be underweight. If the BMI value is greater than 25, the person is considered to be
overweight.

11. Time Calculator
Write a program that asks the user to enter a number of seconds, and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should display the number of minutes in that manyseconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should display the number of hours in that
many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
than or equal to 86,400, the program should display the number of days in that many
seconds
'''