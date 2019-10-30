'''
Please complete the following questions. Mess around with formatting as much as possible, 
use the 3 methods of formatting that we learned. Old % formatting, str.format(), and 
formatted string literals( print (f’ ‘) ). Refer to your notes or the python docs to get 
examples on how to do each.

https://docs.python.org/3/tutorial/inputoutput.html 

 1. Write a program that displays the following information:
	• Your name
	• Your address, with city, state, and ZIP
	• Your telephone number
	• Your MOS
'''
"""
print(f'My name')
print("{!s} {!s}".format("My address, with", "city, state, and ZIP"))
print("Your telephone number".format(end=""))
print("Your MOS")
"""

'''
2.  A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, and then displays
the profit that will be made from that amount.
'''

"""
sales = input("Enter projected sales: ")
profit = float(sales) * .23
print('Your projected profit is ${:0,.2f}'.format(profit))
"""

'''
3.  One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
enter the total square feet in a tract of land and calculates the number of acres in the tract.
'''

"""
feet = input("Enter total sq ft: ")
acre = int(feet) / 43560
print('If SqFt = {}, then Acres = {:.2f}'.format(feet, acre))
"""

'''
 4. A customer in a store is purchasing five items. Write a program that asks for the price of
each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 6 percent.
'''

"""
item1 = input("Enter price of 1st item: ")
item2 = input("Enter price of 2nd item: ")
item3 = input("Enter price of 3rd item: ")
item4 = input("Enter price of 4th item: ")
item5 = input("Enter price of 5th item: ")

subtotal = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)
tax = subtotal * .06
total = tax + subtotal


print(f"The Subtotal is ${subtotal:.2f}\nThe Sales tax is ${tax:.2f}\nThe Total is ${total:.2f1}")
"""

'''
5.  Assuming there are no accidents or delays, the distance that a car travels down the interstate can 
be calculated with the following formula:
Distance = Speed * Time

 A car is traveling at 60 miles per hour. Write a program that displays the following:
	• The distance the car will travel in 5 hours
	• The distance the car will travel in 8 hours
	• The distance the car will travel in 12 hours
'''

"""
def getDistance(time):
    return 60*time

print(f"The distance the car will travel in 5 hours: {getDistance(5)} miles\nThe distance \
the car will travel in 8 hours: {getDistance(8)} miles\nThe distance the car will travel in \
12 hours: {getDistance(12)} miles\n")
"""

'''
6.  Write a program that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 4 percent
and the county sales tax is 2 percent. The program should display the amount of the purchase, 
the state sales tax, the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).
'''
"""
purchase = float(input("Enter amount of purchase: "))

stateTax = purchase * .04
countyTax = purchase * .02
totalTax = stateTax + countyTax
total = purchase + totalTax

print(f"The Purchase amount is ${purchase:.2f}\nThe State Sales tax is ${stateTax:.2f}\nThe \
county Sales tax is ${countyTax:.2f}\nThe Total tax is ${totalTax:.2f}\nThe Total cost \
is ${total:.2f}")
"""

'''
7.  A car’s miles-per-gallon (MPG) can be calculated with the following formula:
 MPG = Miles driven / Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car’s MPG and display the result.
'''

"""
milesDriven = float(input("Enter # of miles driven: "))
gallonsUsed = float(input("Enter # of gallons used: "))

print(f"The MPG is {(milesDriven/gallonsUsed):.2f} miles per gallon")
"""

'''
8.  Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, and then calculate the amount
of a 15 percent tip and 7 percent sales tax. Display each of these amounts and the total.
'''

"""
foodCost = float(input("Enter the amount of the meal: $"))

tip = foodCost * .15
salesTax = foodCost * .07
total = foodCost + salesTax + tip

print(f"The Purchase amount is ${foodCost:.2f}\nThe 15% tip is ${tip:.2f}\nThe \
sales tax is ${salesTax:.2f}\nThe Total cost is ${total:.2f}")
"""

'''
9. Write a program that converts Celsius temperatures to Fahrenheit temperatures. 
The formula is as follows:

 F = (9/5)C + 32

The program should ask the user to enter a temperature in Celsius, and then display the
temperature converted to Fahrenheit.
'''

"""
celTemp = float(input("Enter temperature in Celcius: "))
fahTemp = (9/5)*celTemp + 32

print(f"{celTemp:.0f} degrees Celcius is {fahTemp:.0f} degrees Fahrenheit.")
"""

'''
10.  Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 1,000.
• When Joe purchased the stock, he paid $32.87 per share.
• Joe paid his stockbroker a commission that amounted to 2 percent of the amount he paid
for the stock.
Two weeks later Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 1,000.
• He sold the stock for $33.92 per share.
• He paid his stockbroker another commission that amounted to 2 percent of the amount
he received for the stock.

 Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount that Joe sold the stock for.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount is positive, then Joe made a profit. If the amount is
negative, then Joe lost money
'''

def getBuySellInfo():
    #function to get info from user on Cost per share, and num of shares for buy and sell
    buyTotal = (float(input("Enter number of shares purchased: "))  
        * float(input("Enter cost per share when purchased: ")))

    sellTotal = (float(input("Enter number of shares sold: "))
        * float(input("Enter cost per share when sold: ")))
    return (buyTotal, sellTotal)

def getMathAndOutput(buyTotal, sellTotal):
    #function to compute math portions and Display outPut
    buyComm = buyTotal * .02
    sellComm = sellTotal * .02
    profit = sellTotal - buyTotal - sellComm - buyComm

    #Display data
    print(f"\nThe total paid for the stock is ${buyTotal:.2f}\nThe buying commision \
    is ${buyComm:.2f}\nThe amount the stock sold for is ${sellTotal:.2f}\nThe selling \
    commision is ${sellComm:.2f}\n\nAmount of your money left is ${profit:.2f}")

    #find out is profit was made or lost
    if profit > 0:
        print(f'You made a profit!')
    else:
        print(f"You lost money!")

bTotal, sTotal = getBuySellInfo()
getMathAndOutput(bTotal, sTotal)