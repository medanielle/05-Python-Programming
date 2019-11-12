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
next
"""

class Employee:
    def __init__(self, name, id_num, dept, job):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job = job

    def __str__(self):
        return f'\nName: {self.__name}\nId Num: {self.__id_num}\nDept: {self.__dept}\nJob Title: {self.__job}'

