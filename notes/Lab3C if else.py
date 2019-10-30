"""
In Class Example
any employee works over 40 per week, overtime =1.5x normal pay
calc employee gross pay + overtime wages
"""

# this main function to get input from user (hours worked and pay rate)
# and return the gross pay and overtime pay if applicable


def main():
    hours = float(input("Enter number of hours worked this week: "))
    payRate = float(input("Enter payRate in $/hour: "))

    normalHours, overTimeHours = getHours(hours)
    gPay, oPay = getWages(normalHours, overTimeHours, payRate)

    print(f'\nYour over time pay is ${oPay:.2f}.\nYour gross pay is ${gPay:.2f}\n')
    return

def getHours(time):
    # this function reviews the inputs from user and then assignes values to 
    # the hours of Overtime variable and the base pay variable
    if time <= 40:
        normalTime = time
        overTime = 0
    else:
        normalTime = 40
        overTime = time - 40
    return (normalTime, overTime)

def getWages(nTime, oTime, pRate):
    # this function calculates the overtime pay, and the regular pay earned
    oTimePay = oTime * 1.5 * pRate
    grossPay = (nTime*pRate) + oTimePay
    return (grossPay, oTimePay)

main()













'''
Instructions
Create a text-based game where the user is navigating through a "Fun" House. Prompt the user 
to make a decision and using if/elif/else statements, give them different outcomes based on 
their answers. Begin with an introduction to your fun house and prompt the user to choose 
between at least three different options. You can use nested if/elif/else statements to make 
the game more complex.

Requirments
Adhere to PEP8 (Comments, formatting, style, etc)
Utilize userinput
Utilize proper formatting
Utilize proper and clean if/elif/else statements
Follow instructions above

Additional
Take this a step further. Use some previous concepts. Here are some things you can do:
    Create a file that holds all of your prompts
    Store file prompts into a list, dict, etc
    Use if/elif/else statements to validate user input
    Use formatting to create UI elements and/or fancy prompts
    Use operators and user input to perform calculations based on prompts 
Example:

print "Welcome to Fun House! Choose door 1, 2, or 3..."

input = raw_input("> ")

if input == "1":
    #<code>
    print"1"

elif input == "2":
    #<code>
    print "2"

elif input == "3":
    #<code>
    print "3"
else:
    print "Go home you're drunk."
'''