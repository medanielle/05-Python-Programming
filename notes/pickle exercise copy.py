"""​
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.
​"""
import pickle
FILE = 'contacts.txt'
ERROR = 'Entry Not Found!'

def main():
    # set up variable for loop and start loop
    option = 1
    while option != 0:
        # get user's task from menu
        option = display_menu()

        # get GAL from contacts.txt thru function
        gal = read_contacts()

        # open in non closing way
        with open(FILE, 'wb') as out:
            # decision on which function base on user input
            if option == 1:
                look_up(gal)
            elif option == 2:
                gal = new_contact(gal)
            elif option ==3:
                gal = change_email(gal)
            elif option == 4:
                gal = delete_contact(gal)
            # write changes to file in binary
            pickle.dump(gal, out)
        print('\n', read_contacts())                      #DEBUG


def display_menu():
    test = ['0','1', '2', '3', '4']
    task = 'o'
    while task not in test:
        #display menu and return choice
        task =  input("\nDo you want to: \n0 ===>> EXIT Program\n1. Look up a person’s email address \t\t(enter 1)\n2. " 
                        "Add new contact to the GAL \t\t\t(enter 2)\n3. Change an existing email \t\t\t"
                        "(enter 3)\n4. Delete an existing name\\email address \t(enter 4)\n")
        if task in test:
            return int(task)
        else:
            #error checking
            print('\nBad Input! Please enter a number (0-4)')
            


def read_contacts():
    # get GAL from contacts.txt thru function
    gal = {}
    # open in non closing way
    with open(FILE, 'rb') as f:
        end_of_file = False
        # read to the end of the file
        while not end_of_file:
            try:
                # unpickle the next object
                gal.update(pickle.load(f))
            except EOFError:
                # set the flag to indicate the end of the file has been reached
                end_of_file = True
    return gal


def look_up(p_gal):
    answer = ERROR
    while answer == ERROR:
        #get input on what to look up from user and search for string with .get
        search = (input('Enter name to search for: ')).lower()    
        answer = p_gal.get(search, ERROR)
        # if the answer is found display or keep looping
        if answer != ERROR:
            print(f"{search.title()}'s email address is {answer}")
        else:
            print('Try Again!', answer, 'Below are available names:')
            printContacts(p_gal)


def new_contact(p_gal):
    answer = ''
    while answer != ERROR:
        # get data for a person to store it in a dict
        name = input('Name:').lower()
        answer = p_gal.get(name, ERROR)
        # if the answer is not found add contact or keep looping
        if answer == ERROR:
            p_gal.update({name: input('email:').lower()})
        else:
            print(f'The contact ({name.title()}) already exists, below are the names in directory:')
            printContacts(p_gal)
    return p_gal


def change_email(p_gal):
    answer = ERROR
    while answer == ERROR:
        # get key to search for, then search with .get
        search = input('Enter name to change: ').lower()
        answer = p_gal.get(search, ERROR)
        # get email from user for name if found or keep looping
        if answer != ERROR:
            p_gal[search] = input("What is the new email? ").lower()
        else:
            print('Try Again!', answer, 'Below are available names:')
            printContacts(p_gal)
    return p_gal


def delete_contact(p_gal):
    answer = ERROR
    while answer == ERROR:
        search = input('Enter name to delete: ').lower()
        # remove key and value from dict
        answer = p_gal.pop(search, ERROR)
        # display output
        if answer != ERROR:
            print(f'{search} and {answer} contact removed!')
        else:
            print('Try Again!', answer, 'Below are available names:')
            printContacts(p_gal)
    return p_gal


def printContacts(p_gal):
    for item in p_gal:
        print(item.title(), end=',   ')
    print()

main()


"""
​
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the 
dictionary from the file and unpickle it.
​
"""
​
# This program maintains a dictionary binary file that stores names and emails and allows a user to interact with the data in the file
# import the cool things
import pickle
import pprint
import sys
import time
# establish a global variable
user_choice = 5
​
# define main
def charles():
    # call the global variable
    global user_choice
    # Open output file
    output_file = open('name_email.dat', 'rb+')
    # set end of file to false so that it will try the things
    end_of_file = False
    # loop to open the pickle load
    while end_of_file == False:
        # try to do the pickle load
        try:
            name_email = pickle.load(output_file)
        # If it wont work then move on
        except: 
            end_of_file = True
    # show the first display to get user choice
    first_display(user_choice)
    # send user choice to the dictionary to allow user to interact with dictionary
    menu(user_choice, name_email)
    # pickle the dictionary to the file
    pickle.dump(name_email, output_file)
    # close the file
    output_file.close()
# define the first display for user selection
def first_display(user_choice):
    # Display the different options to the user
    print("\n Choose an option")
    print("\n 1 to look up an email address, \n 2 to add a new name and email")
    print(" 3 to change an existing email and \n 4 to delete an existing name and email")
    print(" 5 to display all names and emails \n 0 to quit")
# define the function to print slow
def print_slow(txt):
    # for every letter in whatever text
    for letter in txt:
        # makes it print like typing
        sys.stdout.write(letter)
        # make it print right
        sys.stdout.flush()
        # give the user some time to read
        time.sleep(0.1)
​
# define the menu
def menu(user_choice, name_email):
    # make an attempt to do things
    try:
        # get user choice as an integer
        user_choice = int(input("Enter choice: "))
    # if there is an issue with what the user entered tell them to make a good choice and return to main
    except ValueError:
        print("Make a valid selection 0 to 5: ")
        charles()
    # make it so the selection must be 1 to 5
    while user_choice > 0 and user_choice < 6:
        # user chose 1 to search for an email
        if user_choice == 1:
            # get the name of the person they want to search for
            search = input("Enter the name of the person you want an email for (format is First Last): ").title()
            # if the name exists display the result
            if search in name_email:
                print('The email for', search, 'is ', name_email[search])
            # If the name does not exist ask if they want to add it and tell them to choose option 2
            else:
                print("The email for", search, "was not found.")
                print("If you would like to add it please choose option 2")
        # if user chose 2 then they will add an email to dictionary
        elif user_choice == 2:
            # User enters the name to add
            name_add = input("Enter the First Lastname for the name that needs added: ").title()
            # User enters the email to add
            email_add = input(f"Enter the email for {name_add:}: ")
            # Add the entry to the dictionary
            name_email[name_add] = email_add
            # print/validate the result
            print("You added: ", name_add, ":", name_email[name_add])
        # if the user chose 3 they will be changing the email of someone
        elif user_choice == 3:
            # Get name to edit
            name_edit = input("Enter the name of the person you want to change the email for (format is First Last): ").title()
            # If the name exists then do the edit
            if name_edit in name_email:
                email_edit = input(f'Enter the email you would like to assign for {name_edit:}: ')
                name_email[name_edit] = email_edit
                print("Here is your update: ", name_email[name_edit])
            # If the name does not exist then tell them to choose option 2 to add it
            else:
                print("The email for", name_edit, "was not found.")
                print("If you would like to add it please choose option 2")
        # If the user chose option 4 to remove an email
        elif user_choice == 4:
            # Get the name of the email the user wants to remove
            name_delt = input("Enter the name of the person you want to remove an email for: ").title()
            # If the name exists then remove it from the dictionary
            if name_delt in name_email:
                del name_email[name_delt]
                print("It is done")
            # If the name does not exist then tell the user it was not found
            else:
                print("The email for", name_delt, "was not found.")
        # If the user chose option 5 then display the name email dictionary
        elif user_choice == 5:
            print("Here are all of the names and emails in the record: ")
            # print the dictionary with pprint so that it is nice and perty for the user
            pprint.pprint(name_email, width=1)
        # if the user chose none of those and somehow stayed in the loop then say oops and exit
        else:
            print("oops")
            exit()
        # try to user input
        try:
            # ask the user for more input or to quit
            user_choice = int(input("\n Press 0 to quit and save or make another selection from above: "))
        # if user input was bad and they put data in then it sucks to be them
        except ValueError:
            # if user chose 2, 3, or 4 and then put in a bad input it didnt save
            if user_choice != 5 and user_choice != 1:
                # do the slow print and tell them their issue
                print_slow("Due to your invalid choice all data you put in this session is \n gone, \n done, \n kaput, \n dust. ")
                print_slow("\n Next time make a choice 0 to 5: ")
                exit()
            # if they chose 1 or 5 then loop back to main
            else:
                charles()
# call main
charles()

"""
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.​
"""
​
import pickle
​
def chunn():
    global database
    # try to open the datastore
    try:
        with open('datastore.dat', 'rb') as in_file:
            database = pickle.load(in_file)
    except IOError:
        # if file is missing or does not exist, display the error and start a new database
        print('File has been moved or corrupted.\nInitializing new database:\n')
        database = {}
    
    # Populate a menu for operations
    menu = {
        1 : {'description' : 'Search for an email by a name', 'function' : find_email},
        2 : {'description' : 'Add a new Name and email address', 'function' : add_email},
        3 : {'description' : 'Modify an existing email address', 'function' : modify_email},
        4 : {'description' : 'Remove an entry from the database', 'function' : delete_database_entry},
        5 : {'description' : 'Finish/Quit'}
    }
    # set a flag to continue gathering input for database operations
    menu_select = 0
    # Continuously accept input until user finishes
    while menu_select != 5:
        # add a blank line before the menu print
        print()
        # Display the menu
        for key in menu.keys():
            print(' {} : {}'.format(key, menu[key]['description']))
        # get the user input for their menu option
        menu_select = get_menu_entry()
        # Prompt again until a valid input within the menu keys is entered
        while menu_select not in menu.keys():
            print('Invalid selection')
            menu_select = get_menu_entry()
        # skip function call if menu entry is the same as while loop exit
        if menu_select != 5:
            # call the menu's function
            menu[menu_select]['function']()
​
    # open the file to write the database to
    with open('datastore.dat', 'wb') as out_file:
        pickle.dump(database, out_file)
​
​
def get_menu_entry():
    # Prompt user for menu choice and convert it to an int
    try:
        user_input = int(input('\nEnter the number of the menu option: '))
    except ValueError:
        print('Invalid entry: keyboard input failed to convert to integer')
        # set user_input to 0 for main loop to re-prompt
        user_input = 0
    # return the user_input
    return user_input
​
def find_email():
    # Prompt user for a name, checks if the name is in the database, and prints the email if the key exists
    search = input('Enter the name of the person whose email you wish to find: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # print the person's email
        print(f'\n{search}\'s email:\t{database[search]}')
    else:
        # display no user found in keys
        print(f'\n{search} could not be found.')
​
def add_email():
    # Prompt user for a name and email and add them to the database
    add_name = input('Enter the name to be added: ').title()
    # verify that the name is not in the database keys, otherwise prompt for name again with a unique identifier
    while add_name in database.keys() and add_name != '':
        add_name = input('Name already exists in the database!\nPlease try again or press enter to exit: ').title()
    # if add_name is blank, do nothing otherwise
    if add_name != '':
        # Prompt for the email address to be added
        database[add_name] = input(f'Enter {add_name}\'s email address: ')
    
def modify_email():
    # Prompt user for a name, checks if the name is in the database, and modifies the email if the key exists
    search = input('Enter the name of the person whose email you wish to modify: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # Prompt for the new email address
        database[search] = input(f'Enter the new email address for {search}: ')
    else:
        # display no user found in keys
        print(f'\n{search} could not be found.')
​
def delete_database_entry():
    # Prompt user for a name, checks if the name is in the database, and deletes the entry if the key exists
    search = input('Enter the name of the person whose email you wish to delete: ').title()
    # check if the name is in the database keys
    if search in database.keys():
        # Prompt the user if they really want to delete the entry
        confirmation = input(f'Do you really wish to delete the entry {search}: {database[search]} from the database? (y/n): ')
        # if confirmed yes
        if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
            # delete the entry
            del database[search]
​
# Call the main function
chunn()


import pickle
​
def load_address_book():
    # either we get an existing address book or we start a new, blank one
    try:
        return pickle.load(open(r'D:\tooldev\classwork\python\serialization\address_book2.dat', 'rb'))
    except FileNotFoundError:
        return {}
​
def save_address_book(address_book):
    pickle.dump(address_book, open(r'D:\tooldev\classwork\python\serialization\address_book2.dat', 'wb'))
​
def get_menu_selection():
    print('Welcome to your address book.')
    print('[A] Add')
    print('[D] Delete')
    print('[E] Edit')
    print('[V] View')
    print('[Q] Quit')
​
    return input('What would you like to do? ').lower()
​
# input address book, output address book with new contact
def add_contact(address_book):
    name = input('Name: ')
    email = input('Email: ')
    address_book[name] = email
    print(f"{name} has been added.")
    print('')
    return address_book
​
def delete_contact(address_book):
    name = ''
    error_message = ''
    while name not in address_book:
        # won't print an error until one is generated
        print(error_message)
        name = input('Name to delete: ')
        error_message = f"{name} not found."
    else:
        # del just feels dirty
        del address_book[name]
        print(f"{name} has been deleted.")
        print('')
    return address_book
​
def edit_contact(address_book):
    name = ''
    error_message = ''
    while name not in address_book:
        # won't print an error until one is generated
        print(error_message)
        name = input('Name to edit: ')
        error_message = f"{name} not found."
    else:
        # if found, delete the name you want to edit and just add it
        del address_book[name]
        print(f"Enter information for {name}.")
        return add_contact(address_book)
​
def view_contacts(address_book):
    # iterate and display address_book
    for name, email in address_book.items():
        print(f"{name}")
        print(f"{email}")
        print('')

​
def camarata():
    # load the address book
    address_book = load_address_book()
​
    # what'chu want?
    while True:
        user_menu_selection = get_menu_selection()
​
        # as long as it starts with the appropriate letter
        if user_menu_selection.startswith('a'):
            address_book = add_contact(address_book)
        if user_menu_selection.startswith('d'):
            address_book = delete_contact(address_book)
        if user_menu_selection.startswith('e'):
            address_book = edit_contact(address_book)
        if user_menu_selection.startswith('v'):
            view_contacts(address_book)
        if user_menu_selection.startswith('q'):
            break
​
    # user is here if they broke the loop, save the address book
    save_address_book(address_book)
    exit()
​
camarata()


# Pickle Exercise
# Name and Email Addresses
# for binary conversion and...de...version?
import pickle
# main function is the central hub of functions
def pham():
    name_email = load_data()
    # loops menu until you quit
    while True:
        print(name_email)
        menu(name_email)
# display menu and calls whatever option is selected
def menu(data_dict):
    options = { '1': ["Search", search], 
                '2': ["Add", add], 
                '3': ["Modify", modify], 
                '4': ["Delete", delete],
                '5': ["Quit", quit]}
    user_input = ""
    # prints options
    for k, v in options.items():
        print(f"{k}. {v[0]}")
    # keeps going until valid option is selection
    while user_input not in options:
        user_input = input("To select an option, enter a number: ")
    # warning message of empty data
    if len(data_dict) <= 0:
        print("Warning! Please add more data to have full functionality")
    # call ption selected
    options[user_input][1](data_dict)
# Deletes an entry
def delete(data):
    again = 'y'
    # keeps going as long as user says y and there are items in dict
    while again.lower() == 'y' and len(data) > 0:
        selected = search(data)
        confirm = input(f"{selected.title()}'s email will be deleted. Are you sure? (y/n) ").lower()
        if confirm == 'y':
            data.pop(selected)
            print(f"{selected.title()} has been deleted")
        again = input("Delete more data? (y/n) ")
    # Call save function
    save_data(data)
# modifies selected name's email
def modify(data):
    again = 'y'
    # as long as it's y and data not empty
    while again.lower() == 'y' and len(data) > 0:
        selected = search(data)
        confirm = input(f"{selected.title()}'s email will be modified. Are you sure? (y/n) ").lower()
        if confirm == 'y':
            data[selected] = input("Enter new email address: ").replace("\"", "").replace("\'", "")
        again = input("Modify more data? (y/n) ")
    save_data(data)
# adds item to dictionary and dave when done
def add(data):
    again = 'y'
    new_data = {}
    while again.lower() == 'y':
        name = input("Enter new name: ").lower().replace("\"", "").replace("\'", "")
        if name in data.keys():
            continue
        email = input("Enter their email: ").replace("\"", "").replace("\'", "")
        new_data[name] = email
        again = input("Enter more data? (y/n) ")
    data.update(new_data)
    save_data(data)
# searches for name and dislay details, will return the name
def search(data):
    again = 'y'
    while again ==  'y' and len(data) > 0:
        name = input("Enter a name to look for: ").lower()
        if name not in data:
            print("Sorry, could not find person")
        else:
            print(f"{name.title()}: {data[name]}")
        again = input("Keep searching? (y/n) ").lower()
    return name
# saves data as a binary dat file
def save_data(data):
    f = open('name_email.dat', 'wb')
    pickle.dump(data, f)
    f.close()
# loads a binary dat file
def load_data():
    # end_of_file = False
    # while not end_of_file:
    try:
        f = open('name_email.dat', 'rb')
        data = pickle.load(f)
    except EOFError:
        print(EOFError)
        # end_of_file = True
    except:
        print("Error in loading data")
        # end_of_file = True
    f.close()
    sorted_data = {}
    for k in sorted(data.keys()):
        sorted_data[k] = data[k]
    return sorted_data
​
pham()