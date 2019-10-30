'''
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, and then converts that
distance to miles. The conversion formula is as follows:
Miles =Kilometers * 0.6214 
'''
def getMilesFromKm():
    km = int(input("Enter the kilometers: "))
    return km * 0.6214

#print(f"Converter to miles: {getMilesFromKm():.2f}")
'''
3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings 
for at least 80 percent of the amount it would cost to replace the structure. Write a
program that asks the user to enter the replacement cost of a building and then displays
the minimum amount of insurance he or she should buy for the property. 
'''

def getInsurance():
    replacement = int(input("Enter the cost of replacement: $"))
    return replacement * 0.8

#print(f"You need ${getInsurance():.2f} in insurance")

'''
4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses. 
'''

def getAutoCosts():
    loan_payment = float(input("Enter the monthly loan payment: $"))
    insurance = float(input("Enter the monthly cost of insurance: $"))
    gas = float(input("Enter the monthly cost of gas: $"))
    oil = float(input("Enter the monthly cost of oil: $"))
    tires = float(input("Enter the monthly cost of tires: $"))
    maintenance = float(input("Enter the monthly cost of maintenance: $"))

    monthlyTotal = loan_payment+insurance+gas+oil+tires+maintenance
    annualTotal = monthlyTotal * 12
    print(f'\nMonthly Expenses: ${monthlyTotal:.2f} \nAnnual Expenses: ${annualTotal:.2f}')

#getAutoCosts()

'''
5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 percent of the 
property’s actual value. For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then $0.64 for each $100 of the assessment value. 
The tax for the acre assessed at $6,000 will be $38.40. 
Write a program that asks for the actual value of a piece of property and displays the assessment value and
property tax. 
'''
def getCountyPropTax():
    assessValue = float(input('Enter actual value of property: ')) * .6
    propTax = assessValue * .0064
    print(f'\nAssessment Value: ${assessValue:.2f}\nProperty Tax: ${propTax:.2f}')

#getCountyPropTax()
'''
6. Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The
BMI is often used to determine whether a person is overweight or underweight for his
or her height. A person’s BMI is calculated with the following formula: 
BMI  = weight * 703 / height^2
where weight is measured in pounds and height is measured in inches. 
'''

def getBMI():
    weight = float(input('Enter weight in lbs: '))
    height = float(input('Enter weight in inches: '))
    bmi = weight * 703 / height**2
    print(f'\nBMI: {bmi:.1f}')

#getBMI()
'''
7. Calories from Fat and Carbohydrates
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
calories from fat = fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
calories from carbs = carb grams * 4
The nutritionist asks you to write a program that will make these calculations. 
'''
def getCalFromFat():
    return float(input('Enter your Fat consumption in grams: ')) * 9

def getCalFromCarbs():
    return float(input('Enter your Carb consumption in grams: ')) * 4

#print(f'\nFat Calories = {getCalFromFat()}\nCarb Calories = {getCalFromCarbs()}')
#      f'\nTotal Calories = {(getCalFromCarbs() + getCalFromFat())}')                 this makes multi-line comments!!
'''
8. Stadium Seating
There are three seating categories at a stadium. For a softball game, Class A seats cost $15,
Class B seats cost $12, and Class C seats cost $9. Write a program that asks how many tickets 
for each class of seats were sold, and then displays the amount of income generated from
ticket sales.
'''
def getStadiumSeats():
    my_dict = {15: int(input('Nmmber of Class A seats sold: ')), 
                12: int(input('Nmmber of Class B seats sold: ')),
                9: int(input('Nmmber of Class C seats sold: '))
                }
    totalSales = 0
    for x in my_dict.keys():
        totalSales += x*my_dict[x]
    print(f'\nTotal sales:   ${totalSales:.2f}')

#getStadiumSeats()
'''
9. Paint Job Estimator
A painting company has determined that for every 115 square feet of wall space, one gallon of 
paint and eight hours of labor will be required. The company charges $20.00 per hour for labor. 

Write a program that asks the user to enter the square feet of wall space to be painted and the 
price of the paint per gallon. 

The program should display the followingdata:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job 
'''
#import math for ceil feature
import math

def getPaintEstimate():
    #main program/calls other functions, and then outputs data to screen
    pReq, lhours = getPaintLabor()
    pCost, lCost = getCostCalc(pReq, lhours)
    total = pCost + lCost
    print(f'\nThe number of gallons of paint required: {pReq:.2f}'
        f'\nThe hours of labor required: {lhours:.2f} \nThe cost of the paint: ${pCost:.2f}'
        f'\nThe labor charges: ${lCost:.2f} \nThe total cost of the paint job: ${total:.2f}\n')

def getPaintLabor():
    #get input from user, then calculates and returns # of gallons and hours
    wallSpace = float(input('Enter amount of wall space to be painted: '))
    paintReq = math.ceil(wallSpace/115)
    laborHours = wallSpace/115 * 8
    return paintReq, laborHours

def getCostCalc(p_paint_req, p_labor_hours):
    #calcualte actual cost from amount of paint needed, and returns that data
    paintCost = p_paint_req * float(input("Enter cost for a gallon of paint: "))
    laborCost = p_labor_hours * 20.00
    return paintCost, laborCost

getPaintEstimate()

'''
10. Monthly Sales Tax
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 4 percent
and the county sales tax rate is 2 percent. Write a program that asks the user to enter the
total sales for the month. From this figure, the application should calculate and display the
following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
'''
#declare global variable (set tax amounts)
COUNTY_TAX = .02
STATE_TAX = .04

def getTaxReport():
    #generate output of data for user
    sTax, cTax = getMonthlyCalcs()
    print(f'\nThe amount of county sales tax ${cTax:.2f}\n'
        f'The amount of state sales tax ${sTax:.2f}\n'
        f'The total sales tax: ${(sTax + cTax):.2f}')

def getMonthlyCalcs():
    #calculate indivifual tax amount due
    sales = float(input('Enter total sales for the month: $'))
    stateTax = sales * STATE_TAX
    countyTax = sales * COUNTY_TAX
    return stateTax, countyTax

#getTaxReport()
