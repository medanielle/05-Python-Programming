# Serializing Objects
# called pickle(pickling) in Python
# the process of converting the ogject to a stream of bytes that can be saved to a file for later retrieval 
# turns into binary format, good for storing/transger, remote procedure calls
'''
read
r -- Opens file for read only. File pointer is placed at start of file.
rb -- Opens a file for reading only in binary format. The file pointer is placed at the start of the file.
r+ -- Opens a file for both reading and writing. File pointer is placed at the start of the file.
rb+ -- Opens a file for both reading and writing in binary format. File pointer is placed at the start of the file.

write
w -- Opens a file for writing only. Overwrites the file if it exists. If the file does not exist, it creates a new one.
wb -- Opens a file for writing only in binary format. Overwrites the file if it exists. If it does not exist, it creates a new one.
w+ -- Opens a file for writing and reading. Overwrites the existing file if it exists. If it does not exist, it creates a new one.
wb+ -- Opens a file for writing and reading in binary format. Overwrites the existing file if it exists. If not, it creates a new one.

append
a -- Opens a file for appending. File pointer is at end of file if it exists. If the file does not exist, it creates a new one
ab -- Opens a file for appending in binary format. File pointer is at end of file if it exists. If not, it creates a new one.
a+ -- Opens a file for both appending and reading. If file exists, file pointer placed at end of file. If not, it creates a new one.
ab+ -- Opens a file for both appending and reading in binary format. Follows above file pointer and write rules.

'''

# output_file = open('mydata.dat', 'wb')
# pickle.dump(object, file)

import pickle

def first_pickle():
    # controls loop repitions
    again = 'y'

    # open file for binary writing
    # output_file = open('info.dat', 'wb')

    # open in non closing way?
    with open('info.dat', 'wb') as output_file:
    # get data until user wants to stop
        while again.lower() == 'y':
        # get data about person and save it
            save_data_w_update(output_file)

        # user want more?
            again = input('Enter more data? (y/n)')

    # ALWAYS CLOSE
    # output_file.close()

def save_data(p_file):
    # the save data function gets data about a person and stores it in a dict, then pickles the data to a specific file
    #initialize dict
    person = {}

    # get data for a person to store it in a dict
    person['name'] = input('Name:')
    person['age'] = input('age:')
    person['weight'] = float(input('weight:'))

    # pickle the dict
    pickle.dump(person, p_file)


def save_data_w_update(p_file):
    # the save data function gets data about a person and stores it in a dict, then pickles the data to a specific file
    #initialize dict
    person = {}

    # get data for a person to store it in a dict
    person.update({'name': input('Name:'), 'age': input('age:'), 'weight': float(input('weight:'))})

    # pickle the dict
    pickle.dump(person, p_file)


#first_pickle()

def read_data_unpickle():
    #unpickle the file we created above
    # indicate end of file
    end_of_file = False

    # open a file for binary reading
    #input_file = open('info.dat', 'rb')

    # non closing way 
    with open('info.dat', 'rb') as input_file:

        # read to the end of the file
        while not end_of_file:
            try:
                # unpickle the next object
                person = pickle.load(input_file)

                # display the object
                display_data2(person)

            except EOFError:
                # set the flag to indicate the end of the file has been reached
                end_of_file = True
    
    # close your file
    # input_file.close()

def display_data(p_person):
    #displays the person data that is passed as an object
    print('name: ', p_person['name'])
    print('age', p_person['age'])
    print('weight:', p_person['weight'])
    print()



def display_data2(p_person):
    #displays the person data that is passed as an object
    print(f"name: {p_person['name']}\nage: {p_person['age']}\nweight:{p_person['weight']}")
    print()

#read_data_unpickle()