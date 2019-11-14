"""
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
    Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

"""
from Classes_Exer_class import Pet as pet_class

def pet_func():
    name = input("Enter the Pet's Name: ")
    ani_type = input("Enter the Type of Pet: ")
    age = input("Enter the Pet's Age: ")

    #Create instance of the Cellphone class
    my_pet = pet_class(name, ani_type, age)
    
    #Display the data entered
    print('\nHere is the data you entered')
    print(f"Pet's Name: {my_pet.get_name().title()}")
    print(f"Pet's Type: {my_pet.get_type().title()}")
    print(f"Pet's Age: {my_pet.get_age().title()}")

#pet_func()
"""
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
    Next, design a program that creates a Car object, and then calls the accelerate method
    five times. After each call to the accelerate method, get the current speed of the car and
    display it. Then call the brake method five times. After each call to the brake method, get
    the current speed of the car and display it.
"""
from Classes_Exer_class import Cars as c

def car_func():
    year = input("Enter the Car's Year: ")
    make = input("Enter the Car's Make: ")

    #Create instance of the Cellphone class
    my_car = c(year, make)

    # 5 Loops for accelate
    for x in range(5):
        my_car.accelerate()
        print(f"The car's speed is {my_car.get_speed()}")

    # 5 Loops for braking
    for x in range(5):
        my_car.brake()
        print(f"The car's speed is {my_car.get_speed()}")

#car_func()


"""
3. Personal Information Class
    Design a class that holds the following personal data: name, address, age, and phone number. Write 
    appropriate accessor and mutator methods. Also, write a program that creates
    three instances of the class. One instance should hold your information, and the other two
    should hold your friends’ or family members’ information.
"""
from Classes_Exer_class import Person as p 

def pers_Info():
    my_list = []
    names = ['Danielle', 'Jack', 'Jill']
    addr = ['123 great ln', '456 next rd', '789 final st']
    age = [33, 14, 15]
    phone = ['123-456-7890', '456-789-1230', '789-123-4560']

    for x in range(0, 3):
        each = p(names[x], addr[x], age[x], phone[x])
        my_list.append(each)
        print(each)

#pers_Info()

"""
4. Employee Class
    Write a class named Employee that holds the following data about an employee in attributes: 
    name, ID number, department, and job title.
    Once you have written the class, write a program that creates three Employee objects to
    hold the following data:

Name            ID Number       Department      Job Title
Susan Meyers    47899           Accounting      Vice President
Mark Jones      39119           IT              Programmer
Joy Rogers      81774           Manufacturing   Engineer

The program should store this data in the three objects and then display the data for each
employee on the screen.
"""

from Classes_Exer_class import Employee as e

def employ_Info():
    my_list = []
    names = ['Susan Meyers', 'Mark Jones', 'Joy Rogers']
    depts = ['Accounting', 'IT', 'Manufacturing']
    id_nums = [47899, 39119, 81774]
    jobs = ['Vice President', 'Programmer', 'Engineer']

    for x in range(0, 3):
        each = e(names[x], depts[x], id_nums[x], jobs[x])
        my_list.append(each)
        print(each)

#employ_Info()



"""
5. Retail Item Class
Write a class named RetailItem that holds data about an item in a retail store. The class
should store the following data in attributes: item description, units in inventory, and price.
Once you have written the class, write a program that creates three RetailItem objects
and stores the following data in them:

            Description     Units in Inventory  Price
Item #1     Jacket          12                  59.95
Item #2     Designer Jeans  40                  34.95
Item #3     Shirt           20                  24.95
"""
from Classes_Exer_class import RetailItem as r 

def retail():
    my_list = []
    desc = ['Jacket', 'Designer Jeans', 'Shirt']
    units = [12, 40, 20]
    price = [59.95, 34.95, 24.95]

    for i in range(3):
        this_obj = r(desc[i], units[i], price[i])
        my_list.append(this_obj)
        print(f"Item #{i+1}")
        print(this_obj)
    
    print(f"\t\t Description \t Units \t  Price")

    for x in range(len(my_list)):
        print(f"Item #{x+1} \t{my_list[x].get_desc():>9} {my_list[x].get_units():>10} {my_list[x].get_price():>12}")
        
    
#retail()

"""
6. Employee Management System
    This exercise assumes that you have created the Employee class for Programming Exercise 4.
    Create a program that stores Employee objects in a dictionary. Use the employee ID number
    as the key. The program should present a menu that lets the user perform the following actions:
        • Look up an employee in the dictionary
        • Add a new employee to the dictionary
        • Change an existing employee’s name, department, and job title in the dictionary
        • Delete an employee from the dictionary
        • Quit the program
    When the program ends, it should pickle the dictionary and save it to a file. Each time the
    program starts, it should try to load the pickled dictionary from the file. If the file does not
    exist, the program should start with an empty dictionary.
"""
from Classes_Exer_class import Employee as employ
import pickle

def manage_employees():
    #intialize global varibal and read file into it
    global employ_dict
    employ_dict = read_pickle()

    # start loop and set varibale to end loop
    choice = '0'
    while choice != '5':
        display_dict()
        choice = check_choice()
        if choice == '1':
            search_employee()
        elif choice == '2':
            new_employee()
        elif choice == '3':
            change_employee()
        elif choice == '4':
            del_employee()
        save_pickle()
    #new_dict = read_pickle()
    #print(new_dict)
    
def display_menu():
    # Display the menu, return input
    choice = input(f"\n1. Look up an employee in the dictionary\n2. Add a new employee to the dictionary\n3. Change an existing employee’s name, department, and job title in the dictionary\n4. Delete an employee from the dictionary\n5. Quit the program\n")
    return choice

def check_choice():
    num = display_menu()
    while num not in ['1', '2', '3', '4', '5']:
        print('\nMUST ENTER A NUMBER 1-5!!!')
        num = display_menu()
    return num

def display_dict():
    #Display the dictionary
    print(f"name \t\t id_num \t  Dept \t\t Title")
    for key in employ_dict:
        print(f"{employ_dict[key].get_name()} \t{employ_dict[key].get_id_num()} \t{employ_dict[key].get_dept()} \t\t{employ_dict[key].get_job()}")

def my_search(search):
    #simplify search?
    if search in employ_dict:
        return True
    else:
        return False

def search_employee():
    # get search paramenter and if found display, other wise error
    search = input('Enter ID Number to Search for: ')
    if my_search(search) == True:
        print('I found it!')
        print(employ_dict[search])
    else:
        print("ID not found!")

def new_employee():
    #get seach parameter then add if num not in database yet
    id_num = input('Enter ID Number of new employee: ')
    if my_search(id_num) == True:
        print('That ID num already exits, please return to main menu and try again')
    else:
        employ_dict[id_num] = employ(input('Name of new employee: '), id_num, input('Dept of new employee: '), input('Title of new employee: '))

def change_employee():
    # get search paramenter, if found then change info, if not return to menu
    id_num = input('Enter ID Number of employee to update: ')
    if my_search(id_num) == True:
        print(employ_dict[id_num])
        employ_dict[id_num] = employ(input('Updated name of employee: '), id_num, input('Updated Dept of employee: '), input('Updated Title of employee: '))
    else:
        print("That ID num doesn't exits, please return to main menu and try again")

def del_employee():
    # get search paramete, then del if found, or return to menu
    id_num = input('Enter ID Number of employee to delete: ')
    if my_search(id_num) == True:
        del employ_dict[id_num]
    else:
        print("That ID num doesn't exits, please return to main menu and try again")

def read_pickle():
    # either we get an existing address book or we start a new, blank one
    try:
        with open('employee.txt', 'rb') as f:
            employ_dict = pickle.load(f)
        return employ_dict
    except FileNotFoundError:
        print('******** FILE WASNT FOUND ********')
        return {}

def save_pickle():
    with open('employee.txt', 'wb') as f:
        pickle.dump(employ_dict, f)

#manage_employees()

"""
7. Cash Register
    This exercise assumes that you have created the RetailItem class for Programming
    Exercise 5. Create a CashRegister class that can be used with the RetailItem class. The
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
    Demonstrate the CashRegister class in a program that allows the user to select several
    items for purchase. When the user is ready to check out, the program should display a list
    of all the items he or she has selected for purchase, as well as the total price.
"""
from Classes_Exer_class import RetailItem  
from Classes_Exer_class import CashRegister as register

def retail_register():
    global my_items
    my_items = []
    global reg_obj
    reg_obj = register()
    desc = ['Jacket', 'Jeans', 'Shirt']
    units = [12, 40, 20]
    price = [59.95, 34.95, 24.95]

    for i in range(3):
        this_obj = RetailItem(i+1, desc[i], units[i], price[i])
        my_items.append(this_obj)
    
    num = 0
    while num != '5':
        num = check_num()
        if num == '1':
            display_wares(my_items)
        if num == '2':
            add_cart()
        if num == '3':
            display_wares(reg_obj.get_purchase_list())
        if num == '4':
            print(f'The total cost of cart: ${reg_obj.get_total():.2f}')

def display_options():
    # Display the menu, return input
    choice = input(f"\n1. See available items\n2. Add a new item to cart\n3. Show items in cart\n4. Get total cost\n5. Quit the program\n")
    return choice

def check_num():
    num = display_options()
    while num not in ['1', '2', '3', '4', '5']:
        print('\nMUST ENTER A NUMBER 1-5!!!')
        num = display_options()
    return num

def display_wares(my_items):
    print(f"\n\t\t Description \t Units \t  Price")
    for item in my_items:
        print(item)
        #print(f"Item #{p_my_list[x].get_id_num} \t{p_my_list[x].get_desc():>9} {p_my_list[x].get_units():>10} {p_my_list[x].get_price():>12}")

def add_cart():
    item = int(input('Enter Item Num: '))
    reg_obj.purchase_item(my_items[item-1])
 
#retail_register()

"""
8. Trivia Game
    In this programming exercise you will create a simple trivia game for two players. The program will 
    work like this:
        • Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
        should be a total of 10 questions.) When a question is displayed, 4 possible answers are
        also displayed. Only one of the answers is correct, and if the player selects the correct
        answer, he or she earns a point.
        • After answers have been selected for all the questions, the program displays the number
        of points earned by each player and declares the player with the highest number of points
        the winner.
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
    The program should have a list or a dictionary containing 10 Question objects, one for
    each trivia question. Make up your own trivia questions on the subject or subjects of your
    choice for the objects.
"""
import random
from Classes_Exer_class import Questions as q 

def trivia_game():
    # set up dictionary as global, read pickled dictionary
    global ques_dict
    ques_dict = read_pickle_2()
    
    player1_pts = 0
    player2_pts = 0

    # iterate through whole dictionary
    for x in range(10):
        #player 1 gets even question (player 2 = odd)
        if x % 2 == 0:
            print(f'\nPlayer 1:')
            player1_pts += do_ques(ques_dict[random.randint(0, 19)])
        else:
            print(f'\nPlayer 2:')
            player2_pts += do_ques(ques_dict[random.randint(0, 19)])

    display_winner(player1_pts, player2_pts)

    save_pickle_2()

def display_winner(p1_pts, p2_pts):
    # display winner and total
    if p1_pts > p2_pts:
        print("Player 1 WON!!")
    elif p2_pts > p1_pts:
        print("Player 2 WON!!")
    else:
        print("Its a TIE! Boo!")
    print(f'\nPlayer 1: {p1_pts}\nPlayer 2: {p2_pts}')

def do_ques(p_value):
    print(f'\n{p_value.get_question()}\n')
    for each in p_value.get_answers():
        print(each)
    guess = check_guess()
    if p_value.get_correct() == guess:
        print("That's Right!")
        points = 1
    else:
        print(f"That's Wrong! Correct Answer: {p_value.get_correct()}")
        points = 0
    return points

def check_guess():
    num = input('\nYour Answer: ')
    while num not in ['1', '2', '3', '4']:
        print('\nMUST ENTER A NUMBER 1-4!!!')
        num = input('\nYour Answer: ')
    return num

def read_pickle_2():
    # either we get an existing address book or we start a new, blank one
    try:
        with open('questions.txt', 'rb') as f:
            ques_dict = pickle.load(f)
        return ques_dict
    except FileNotFoundError:
        print('******** FILE WASNT FOUND ********')
        return {}

def save_pickle_2():
    with open('questions.txt', 'wb') as f:
        pickle.dump(ques_dict, f)

#trivia_game()

    '''
    count = 0
    questions = [['What do herpetologists study?', ['1. Herpes', '2. Blood', '3. Reptiles and amphibians', '4. Insects'], '3'], ['What is the function of mitochondria in the cell?', ['1. To generate energy', '2. To process waste', '3. To kill viruses or other antigens', '4. To repair damage'], '1'], ['What is Andromeda?', ['1. A bacteria that can cause death', '2. An array of radio telescopes', '3. An element of the Periodic Table', '4. The nearest major galaxy to the Milky Way '], '4'], ['What is the largest moon in the Solar System?', ["1. The Earth's Moon", '2. Ganymede ', '3. Pluto', '4. Europa'], '2'], ['How long does it take light to travel from the Sun to the Earth?', ["1. It's instantaneous", '2. About 11 days', '3. About 8 minutes', '4. 2-3 months, depending on the time of year'], '3'], ['Which of these noble ranks is highest?', ['1. Baron', '2. Earl', '3. Marquis', '4. Duke'], '4'], ['The U.S. state of New Jersey is named after Jersey. But what is Jersey?', ['1. A British island off the coast of France', '2. A Dutch province', '3. A Native American tribe', '4. There are multiple theories - no one is sure'], '1'], ['Who killed Greedo?', ['1. Hannibal Lecter', '2. Han Solo', '3. Hermione Granger', '4. Hercules'], '2'], ['How many moons does Mars have?', ['1. 1', '2. 2', '3. 3', '4. None'], '2'], ['Which of these is NOT caused by a virus?', ['1. Smallpox', '2. Cholera', '3. Measles', '4. Herpes'], '2'], ['What is a pomelo?', ['1. An old-fashioned punching bag', '2. A breed of dog', '3. The largest citrus fruit ', '4. Something that cheerleaders hold'], '3'], ['In the nursery rhyme, how many blackbirds were baked in a pie?', ['1. 4', '2. 11', '3. 24', '4. 99'], '3'], ['What are the main colors on the flag of Spain?', ['1. Black and yellow', '2. meh', '3. Really Stupid', '4. Correct'], '4'], ['What is Question 14?', ['1. stupid', '2. Correct', '3. meh', '4. Really Stupid'], '2'], ['What is Question 15?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3'], ['What is Question 16?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3'], ['What is Question 17?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3'], ['What is Question 18?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3'], ['What is Question 19?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3'], ['What is Question 20?', ['1. stupid', '2. meh', '3. Correct', '4. Really Stupid'], '3']]
    for each in questions:
        this_obj = q(each[0], each[1], each[2])
        print(this_obj)
        ques_dict.update({count: this_obj})
        count +=1
    
    print(len(ques_dict))
    #for key, value in ques_dict.items():
        #print(key)
        #print(value)
    """

"""
player1_pts = 0
    player2_pts = 0

    # iterate through whole dictionary
    for key, value in ques_dict.items():
        #player 1 gets even question (player 2 = odd)
        if key % 2 == 0:
            print(f'\nPlayer 1:')
            player1_pts += do_ques(value)
        else:
            print(f'\nPlayer 2:')
            player2_pts += do_ques(value)

    display_winner(player1_pts, player2_pts)
    
    save_pickle_2()
"""
