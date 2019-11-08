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

def main():
    # set up variable for loop 
    again = 'y'
    
    #start loop
    while again.lower() == 'y':
        # get user's task from menu
        option = display_menu()
        # decision base on what input was
        if option == 1:
            look_up()
        elif option == 2:
            new_contact()
        elif option ==3:
            change_email()
        elif option == 4:
            delete_contact()
        else:
            #error checking
            print('Bad Input! Please enter a number (1-4)')
        print(read_contacts())                      #DEBUG
        # user want more?
        again = input('Display Menu again? (y/n)')


def display_menu():
    #display menu and return choice
    task = int(input("Do you want to: \n1. Look up a person’s email address \t\t(enter 1)\n2. Add new contact to the GAL \t\t\t(enter 2)\n3. Change an existing email \t\t\t(enter 3)\n4. Delete an existing name\\email address \t(enter 4)\n"))
    return task


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


def look_up():
    # get GAL from contacts.txt thru function
    gal = read_contacts()
    #get input on what to look up from user
    search = input('Enter name to search for: ')
    # search for string with .get
    answer = gal.get(search, 'Entry Not Found')
    # if the answer is found display or have them go back to menu
    if answer != 'Entry Not Found':
        print(f"{search}'s email address is {answer}")
    else:
        print('Try Again!', answer)



def new_contact():
    # get GAL from contacts.txt thru function
    gal = read_contacts()
    # open in non closing way
    with open(FILE, 'ab') as out:
        # get data for a person to store it in a dict
        gal.update({input('Name:'): input('email:')})
        # pickle the dict
        pickle.dump(gal, out)


def change_email():
    # get GAL from contacts.txt thru function
    gal = read_contacts()
    # open in non closing way
    with open(FILE, 'ab') as out:
        # get key to search for
        search = input('Enter name to change: ')
        # search with .get
        answer = gal.get(search, 'Entry Not Found')
        # display output
        if answer != 'Entry Not Found':
            gal[search] = input("What is the new email? ")
        else:
            print('Try Again!', answer)
        # write changes to file in binary
        pickle.dump(gal, out)


def delete_contact():
    # delete contact with pop
    # get GAL from contacts.txt thru function
    gal = read_contacts()
    # open in non closing way
    with open(FILE, 'ab') as out:
        search = input('Enter name to delete: ')
        # remove key and value from dict
        answer = gal.pop(search, 'Entry Not Found')
        # display output
        if answer != 'Entry Not Found':
            print(f'{answer} contact removed!')
        else:
            print('Try Again!', answer)
        # write changes to file in binary
        pickle.dump(gal, out)


main()
