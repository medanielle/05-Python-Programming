"""
3. 
(The Triangle class) Design a class named Triangle that extends the
GeometricObject class defined below. The Triangle class contains:
    - Three float data fields named side1, side2, and side3 to denote the three
    sides of the triangle.
    - A constructor that creates a triangle with the specified side1, side2, and
    side3 with default values 1.0.
    - The accessor methods for all three data fields.
    - A method named getArea() that returns the area of this triangle.
    - A method named getPerimeter() that returns the perimeter of this triangle.
    - A method named __str__() that returns a string description for the triangle.

    Write a test program that prompts the user to enter the three sides of the 
    triangle, a color, and 1 or 0 to indicate whether the triangle is filled. 
    The program should create a Triangle object with these sides and set the 
    color and filled properties using the input. The program should display the 
    triangle’s area, perimeter, color, and True or False to indicate whether the 
    triangle is filled or not.
"""

class GeometricObject:
    # initalize attributes 
    def __init__(self, color = "green", filled = True):
        self.color = color
        self.filled = bool(filled)

    #accessors
    def getColor(self):
        return self.color

    def isFilled(self):
        return bool(self.filled)

    #mutators
    def setColor(self, color):
        self.color = color

    def setFilled(self, filled):
        self.filled = filled

    # why isn't this __str__?
    def toString(self):
        return "color: " + self.color + " and filled: " + str(self.filled)

class Triangle(GeometricObject):
    # initalize attributes and get superclasses's attributes
    # i brought over the superclasses defaults as well
    def __init__(self, color = "green", filled = True, side1=1.0, side2=1.0, side3=1.0):
        GeometricObject.__init__(self, color, filled)  #super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    # accessors
    def get_side1(self):
        return self.__side1
    
    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    # method to find the area of triangle using Heron's formula 
    def getArea(self):
        # area = sqrt(s(s-a)(s-b)(s-c)) where s is the semi-perimeter 
        # of the triangle semi-perimeter = (a+b+c)/2
        
        # set variables to sides provided for this object
        a = float(self.__side1)
        b = float(self.__side2)
        c = float(self.__side3)

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area
    
    def getPerimeter(self):
        # perimeter is all the sides of a triangle added together
        return float(self.__side1) + float(self.__side2) + float(self.__side3)

    def __str__(self):
        # method to return a string of all attributes/methods in this class
        return f"Area: {self.getArea():.2f} Perimeter: {self.getPerimeter()} Color: {self.color} Filled: {self.isFilled()}"


def main():
    # get data from user, place in variables
    color = input("Enter Triangle's color: ")
    filled = int(input('Is it filled? 0 for no | 1 for yes: '))
    a = input('Enter first side: ')
    b = input('Enter second side: ')
    c = input('Enter third side: ')

    # create object with variables created above
    my_tri = Triangle(color, filled, a, b, c)
    # print the string of all the info for the user
    print(my_tri.__str__())

main()

