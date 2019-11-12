import cellphone_class as c

def first():
    # get phone data
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the price: '))

    #Create instance of the Cellphone class
    phone = c.Cellphone(man, mod, retail)

    #Display the data entered
    print('Here is the data you entered')
    print(f'manufacturer: {phone.get_manufact()}')
    print(f'model number: {phone.get_model()}')
    print(f'retail price: ${phone.get_retail_price():,.2f}')

#first()

#this program creates five Cellphone objects and stores them in a list

def cell_list():
    # get a list of CellPhone
    phones = make_list()

    # Display the data in the list
    print('Here is the data you entered: ')
    display_list(phones)

# the make_list function gets data from the user for 5 phones. the function returns a list of cellphone objects containing the data
def make_list():
    # create empty list
    phone_list = []

    # add five cellphone objects to the list
    print('Enter data for five phones.')
    for count in range(1,6):
        #get pohone data
        print('Phone number: ' + str(count) + ': ')
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the price: '))
        print()
        
        #create a new cellphone object in memory and assign it to the new phone variable
        phone = c.Cellphone(man, mod, retail)

        # add object to list
        phone_list.append(phone)

    #return the list
    return phone_list

def display_list(p_list):
    count = 1
    for phone in p_list:
        print(f'Phone number: {str(count):^8}: ')
        print(f'----------------------')

        print(f'manufacturer: {phone.get_manufact()}')
        print(f'model number: {phone.get_model()}')
        print(f'retail price: ${phone.get_retail_price():,.2f}\n')
        count += 1

cell_list()

