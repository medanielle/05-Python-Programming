'''
1. Pet Class
    Write a class named Pet, which should have the following data attributes:
        • __name (for the name of a pet)
        • __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’,
        and ‘Bird’)
        • __age (for the pet’s age)
        The Pet class should have an __init__ method that creates these attributes. It should also
        have the following methods:
        • set_name
        This method assigns a value to the __name field.
        • set_animal_type
        This method assigns a value to the __animal_type field.
        • set_age
        This method assigns a value to the __age field.
        • get_name
        This method returns the value of the name field.
        • get_type
        This method returns the value of the type field.
        • get_age
        This method returns the value of the age field.
'''
class Pet:
    def __init__(self, name, ani_type, age):
        self.__name = name 
        self.__animal_type = ani_type
        self.__age = age 

    def set_name(self, name):
        self.__name = name 
    
    def set_animal_type(self,ani_type):
        self.__animal_type = ani_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

'''
2. Car Class
    Write a class named Car that has the following data attributes:
        • __year_model (for the car’s year model)
        • __make (for the make of the car)
        • __speed (for the car’s current speed)
        The Car class should have an __init__ method that accept the car’s year model and make
        as arguments. These values should be assigned to the object’s __year_model and __make
        data attributes. It should also assign 0 to the __speed data attribute.
        The class should also have the following methods:
        • accelerate
        The accelerate method should add 5 to the speed data attribute each time it is
        called.
        • brake
        The brake method should subtract 5 from the speed data attribute each time it is called.
        • get_speed
        The get_speed method should return the current speed.
'''

class Cars:
    def __init__(self, model, make, speed=0):
        self.__year_model = model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed
"""
        3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods.
"""

class Person:
    def __init__(self, name, addr, age, phone):
        self.name = name 
        self.addr = addr
        self.age = age 
        self.phone = phone

    def set_name(self, name):
        self.name = name 

    def set_addr(self, addr):
        self.addr = addr

    def set_age(self, age):
        self.age = age
    
    def set_phone(self, phone):
        self.phone = phone

    def __str__(self):
        return f'\nName: {self.name}\nAddr: {self.addr}\nAge: {self.age}\nPhone: {self.phone}'

"""
Name            ID Number       Department      Job Title
"""

class Employee:
    def __init__(self, name, id_num, dept, job):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job = job

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_dept(self, dept):
        self.__dept = dept
    
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    def get_dept(self):
        return self.__dept

    def get_id_num(self):
        return self.__id_num

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'\nName: {self.__name}\nId Num: {self.__id_num}\nDept: {self.__dept}\nJob Title: {self.__job}'

"""
            Description     Units in Inventory  Price

"""
class RetailItem:
    def __init__(self, id_num, desc, units, price):
        self.__id_num = id_num
        self.__desc = desc
        self.__units = units
        self.__price = price

    def set_desc(self, desc):
        self.__desc = desc

    def set_units(self, units):
        self.__units = units
    
    def set_price(self, price):
        self.__price = price

    def get_desc(self):
        return self.__desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price
    
    def get_id_num(self):
        return self.__id_num

    def __str__(self):
        return f'Item #: {self.__id_num}\t {self.__desc}\t\t   {self.__units}\t   ${self.__price:.2f}\t'

'''
Create a CashRegister class that can be used with the RetailItem class. The
    CashRegister class should be able to internally keep a list of RetailItem objects. The
    class should have the following methods:
        • A method named purchase_item that accepts a RetailItem object as an argument.
        Each time the purchase_item method is called, the RetailItem object that is passed as
        an argument should be added to the list.
        • A method named get_total that returns the total price of all the RetailItem objects
        stored in the CashRegister object’s internal list.
        • A method named show_items that displays data about the RetailItem objects stored
        in the CashRegister object’s internal list.
        • A method named clear that should clear the CashRegister object’s internal list.
'''
class CashRegister:
    def __init__(self):
        self.__purchase_list = []
        self.__total = 0

    def purchase_item(self, RetailItem):
        self.__purchase_list.append(RetailItem)

    def get_total(self):
        self.__total = 0
        for each in self.__purchase_list:
            self.__total += each.get_price()
        return self.__total
    
    def show_items(self):
        for each in self.__purchase_list:
            print(each)

    def clear_all(self):
        self.__purchase_list = []
        self.__total = 0

    def get_purchase_list(self):
        return self.__purchase_list
    
    #def __str__(self):
        #return f'Description: {self.__desc}\nUnits: {self.__units}\nPrice: ${self.__price:.2f}\n'

"""
To create this program, write a Question class to hold the data for a trivia question. The
    Question class should have attributes for the following data:
        • A trivia question
        • Possible answer 1
        • Possible answer 2
        • Possible answer 3
        • Possible answer 4
        • The number of the correct answer (1, 2, 3, or 4)
    The Question class also should have an appropriate __init__ method, accessors, and
    mutators.
"""

class Questions:
    def __init__(self, ques, ans_list, correct):
        self.__ques = ques 
        self.__ans_list = ans_list
        self.__correct = correct

    def set_ques(self, ques ):
        self.__ques = ques 

    def set_correct(self, correct):
        self.__correct = correct
    
    def set_ans_list(self, ans_list):
        self.__ans_list = ans_list

    def get_question(self):
        return self.__ques

    def get_answers(self):
        return self.__ans_list
    
    def get_correct(self):
        return self.__correct
    
    #def print_ques(self):
        #return f'\n{self.__ques}'

    def __str__(self):
        return f'\nQ:{self.__ques}\nAL:{self.__ans_list}\nC:{self.__correct}'
