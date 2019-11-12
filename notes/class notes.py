# Class
# 
# A class is code that psecifies the stat attributes and methods for a particular
# class is blue print
# instance is cookie cutter house 1 or 2
"""
>>> class SomeClass:
...     x=100
... 
>>> SomeClass.x
100
>>> someIstance = SomeClass()
>>> someIstance
<__main__.SomeClass object at 0x0000020BB8F90B20>
>>> someIstance.x
100
>>> SomeClass.x = 400
>>> someIstance.x
400
>>> someIstance.x = 1000
>>> SomeClass.x
400
>>> someClass.x = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'someClass' is not defined
>>> SomeClass.x = 0 
>>> SomeClass.x
0
>>> someIstance
<__main__.SomeClass object at 0x0000020BB8F90B20>
>>> someIstance.x              *********************THIS*********
1000
"""
class someClass:
    ex1 = 0
    ex2 = 0
    def f(self, val):
        ex1 = val
        self.ex2 = val
        #print('method EX1', ex1)
# the class has been created. We also created a method.
# the method attempts to change ex1 and self.ex2 to val

def first():
    someInstance = someClass()
    print('Instance 1: ',someInstance.ex1)   # local Variable to the f method
            # output 0
    print('Instance 2: ', someInstance.ex2)     # Instance Variable
            # output 0
    print(someInstance.f(100))
    print('Instance 1 After: ', someInstance.ex1)
            # output 0
    print('Instance 2 After: ',someInstance.ex2)
            # output 100

#first()

#Lab5B

class SuperHero:
    def __init__(self, h_name, r_name, powers= 'None', colors= 'None'):
        self.__h_name = h_name
        self.__r_name = r_name
        self.__powers = powers
        self.__colors = colors

    def set_hero_name(self, h_name):
        # this method accepts an argument for the hero's name
        self.__h_name = h_name

    def set_real_name(self, r_name):
        # this method accepts an argument for the hero's real name
        self.__r_name = r_name

    def set_powers(self, powers):
        # this method accepts an argument for the hero's powers (list)
        self.__powers = powers
    
    def set_colors(self, colors):
        # this method accepts an argument for the hero's colors (list)
        self.__colors = colors

    def get_hero_name(self):
        # this method returns the hero's name
        return self.__h_name
    
    def get_real_name(self):
        # this methodreturns the hero's real name
        return self.__r_name
    
    def get_powers(self):
        # this method returns the hero's powers (list)
        return self.__powers
    
    def get_colors(self):
        # this method returns the hero's colors (list)
        return self.__colors

def lab5B():
    # get phone data
    h_name = input("Enter the Hero's Name: ")
    r_name = input("Enter the Hero's Real Name: ")
    powers = (input("Enter the Hero's Powers (with commas): ")).split(',')
    colors = (input("Enter the Hero's Colors (with commas): "))

    #Create instance of the Cellphone class
    my_hero = SuperHero(h_name,r_name, powers, colors)

    #Display the data entered
    print('\nHere is the data you entered')
    print(f"Hero's Name: {my_hero.get_hero_name().title()}")
    print(f"Hero's Real Name: {my_hero.get_real_name().title()}")
    print(f"Hero's Powers: {my_hero.get_powers()}")
    print(f"Hero's Colors: {my_hero.get_colors().title()}")

lab5B()


rawio +> new diagram +> save to device => blank Diagram => UML
unified modeling language
