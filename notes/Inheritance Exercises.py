"""
1. Employee and ProductionWorker Classes
    Write an Employee class that keeps data attributes for the following pieces of information:
        • Employee name
        • Employee number
    Next, write a class named ProductionWorker that is a subclass of the Employee class. The
    ProductionWorker class should keep data attributes for the following information:
        • Shift number (an integer, such as 1, 2, or 3)
        • Hourly pay rate

    The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the
    night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
    Once you have written the classes, write a program that creates an object of the
    ProductionWorker class and prompts the user to enter data for each of the object’s data
    attributes. Store the data in the object and then use the object’s accessor methods to retrieve it and display it on the screen.

"""
class Employee:
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num
    
    def set_name(self, emp_name):
        self.__emp_name = emp_name
    def set_emp_num(self, emp_num):
        self.__emp_num = emp_num
    def get_name(self):
        return self.__emp_name
    def get_emp_num(self):
        return self.__emp_num

class ProductionWorker(Employee):
    def __init__(self, name, emp_num, shift_num, pay_rate):
        Employee.__init__(self, name, emp_num)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate
    
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    def get_shift_num(self):
        return self.__shift_num
    def get_pay_rate(self):
        return self.__pay_rate
    
    #def __str__(self):
        #return f'\nName: {.__emp_name}\nEmployee Num: {self.__emp_num}\nShift Number: {self.__shift_num}\nPay Rate: {self.__pay_rate}'

def get_prod_work():
    name = input("Enter the Worker's Name: ")
    num = int(input("Enter Worker's Employee NUmber: "))
    shift = int(input("Enter Shift (day=1/night=2): "))
    pay = float(input("Enter Worker's Pay Rate: "))
    #print(name, num, shift, pay)
    prod_worker = ProductionWorker(name, num, shift, pay)
    #print(prod_worker)
    print(f'\nName: {prod_worker.get_name()}\nPay Rate: ${prod_worker.get_pay_rate():.2f}\nEmployee Num: {prod_worker.get_emp_num()}\nShift Number: {prod_worker.get_shift_num()}')

#get_prod_work()
"""
2. ShiftSupervisor Class
    In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
    addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
    production goals. 
    salary
    bonus
    (shift)

    Write a ShiftSupervisor class that is a subclass of the Employee class
    you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
    attribute for the annual salary and a data attribute for the annual production bonus that a
    shift supervisor has earned. Demonstrate the class by writing a program that uses a
    ShiftSupervisor object.

"""
class ShiftSupervisor(Employee):
    def __init__(self, name, emp_num, shift_num, salary, bonus):
        Employee.__init__(self, name, emp_num)
        self.__shift_num = shift_num
        self.__salary = salary
        self.__bonus = bonus
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num
    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = bonus
    def get_bonus(self):
        return self.__bonus
    def get_salary(self):
        return self.__salary
    def get_shift_num(self):
        return self.__shift_num

def get_shift_sup():
    name = input("Enter the Worker's Name: ")
    num = int(input("Enter Worker's Employee NUmber: "))
    shift = int(input("Enter Shift (day=1/night=2): "))
    sal = int(input("Enter Annual Salary: "))
    bonus =  int(input("Enter Production Bonus: "))


    shift_super = ShiftSupervisor(name, num, shift, sal, bonus)


    print(f'\nName: {shift_super.get_name().title()}\nPay Rate: {shift_super.get_salary():,}\nProduction Bonus: {shift_super.get_bonus():,}\nEmployee Num: {shift_super.get_emp_num()}\nShift Number: {shift_super.get_shift_num()}')

# get_shift_sup()
"""

3. Person and Customer Classes
    Write a class named Person with data attributes for a person’s name, address, and telephone number. Next, write a class named Customer that is a subclass of the Person class.
    The Customer class should have a data attribute for a customer number and a Boolean data
    attribute indicating whether the customer wishes to be on a mailing list. Demonstrate an
    instance of the Customer class in a simple program.
    
"""

class Person:
    def __init__(self, name, addr, tele):
        self.__name = name
        self.__addr = addr
        self.__tele = tele
    
    def set_name(self, name):
        self.__name = name
    def set_addr(self, addr):
        self.__addr = addr
    def set_tele(self, tele):
        self.__tele = tele

    def get_tele(self):
        return self.__tele
    def get_addr(self):
        return self.__addr
    def get_name(self):
        return self.__name

class Customer(Person):
    def __init__(self, name, addr, tele, num, mail):
        super().__init__(name, addr, tele)
        self.__num = num
        self.__mail = mail

    
    def set_num(self, num):
        self.__num = num
    def set_mail(self, mail):
        self.__mail = mail

    def get_mail(self):
        return self.__mail
    def get_num(self):
        return self.__num

def get_customer():
    name = input("Name: ")
    addr = input("Mailing address: ")
    tele = input("Telelphone Number: ")
    num = int(input("Customer ID Number: "))
    mail =  bool(int(input("Mailing list? Yes = 1 & No = 0: ")))
    new_cust = Customer(name, addr, tele, num, mail)

    print(f'\nCustomer Info\n----------------\nName: {new_cust.get_name()}\nMailing address: {new_cust.get_addr()}\nTelelphone Number: {new_cust.get_tele()}\nCustomer ID Number: {new_cust.get_num()}\nMailing list: {new_cust.get_mail()}')

get_customer()