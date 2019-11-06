'''
Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the 
courses meet. The dictionary should have the following keyvalue pairs:

Course Number (key) Room Number (value)
CS101               3004
CS102               4501
CS103               6755
NT110               1244
CM241               1411

The program should also create a dictionary containing course numbers and the names of
the instructors that teach each course. The dictionary should have the following key-value
pairs:

Course Number (key) Instructor (value)
CS101               Haynes
CS102               Alvarado
CS103               Rich
NT110               Burke
CM241               Lee

The program should also create a dictionary containing course numbers and the meeting
times of each course. The dictionary should have the following key-value pairs:

Course Number (key) Meeting Time (value)
CS101               8:00 a.m.
CS102               9:00 a.m.
CS103               10:00 a.m.
NT110               11:00 a.m.
CM241               1:00 p.m.

The program should let the user enter a course number, and then it should display the
course’s room number, instructor, and meeting time.
'''
def getCourseInfo():
    room_dict = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    instruct_dict = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    time_dict = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.',
                 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
    course = 'CS101'
    while course not in room_dict.keys():
        course = input(f'Enter Course Number for info. Choose from:\n{room_dict.keys()}\n\nCourse Code: ')
        if course not in room_dict.keys():
            print('Not a vaild')
    print(f'Room Number: {room_dict[course]}\nInstructor: {instruct_dict[course]}\nTime: {time_dict[course]}')

#getCourseInfo()
'''
2. Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.) The program
should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and
incorrect responses. (As an alternative to the U.S. states, the program can use the names of
countries and their capitals.)

capitals_dict ={'Alabama': 'Montgomery', 'Montana': 'Helena', 'Alaska': 'Juneau', 'Nebraska': 'Lincoln',
                    'Arizona': 'Phoenix', 'Nevada': 'Carson City', 'Arkansas': 'Little Rock',
                    'New Hampshire': 'Concord', 'California': 'Sacramento', 'New Jersey': 'Trenton',
                    'Colorado': 'Denver', 'New Mexico': 'Santa Fe', 'Connecticut': 'Hartford',
                    'New York': 'Albany', 'Delaware': 'Dover', 'North Carolina': 'Raleigh', 
                    'Florida': 'Tallahassee', 'North Dakota': 'Bismarck', 'Georgia': 'Atlanta', 'Ohio': 'Columbus',
                    'Hawaii': 'Honolulu', 'Oklahoma': 'Oklahoma City', 'Idaho': 'Boise', 'Oregon': 'Salem',
                    'Illinois': 'Springfield', 'Pennsylvania': 'Harrisburg', 'Indiana': 'Indianapolis',
                    'Rhode Island': 'Providence', 'Iowa': 'Des Moines', 'South Carolina': 'Columbia',
                    'Kansas': 'Topeka', 'South Dakota': 'Pierre', 'Kentucky': 'Frankfort', 'Tennessee': 'Nashville',
                    'Louisiana': 'Baton Rouge', 'Texas': 'Austin', 'Maine': 'Augusta', 'Utah': 'Salt Lake City',
                    'Maryland': 'Annapolis', 'Vermont': 'Montpelier', 'Massachusetts': 'Boston', 'Virginia': 'Richmond',
                    'Michigan': 'Lansing', 'Washington': 'Olympia', 'Minnesota': 'St Paul', 
                    'West Virginia':'Charleston', 'Mississippi': 'Jackson', 'Wisconsin': 'Madison', 
                    'Missouri': 'Jefferson City', 'Wyoming': 'Cheyenne'}
'''
import random

def stateCaps():    
    d = {}
    with open("dict.txt") as f:
        for line in f:
            strip = line.rstrip('\n')
            (key, val) = strip.split('\t')
            d[key] = val
    
    correct = 0
    wrong = 0
    study = []
    answer = 'y'
    while answer != 'q':
        question = random.choice(list(d.keys()))
        answer = input(f"\nState: {question}\nCapital ('q' for quit): ")
        if answer.lower() == str(d[question]).lower():
            print('Correct!')
            correct += 1
        elif answer == 'q':
            continue
        elif answer.lower() != str(d[question]).lower():
            print(f"Wrong! Correct Answer: {d[question]}")
            wrong += 1
            study.append(question)

    print(f'# Correct: {correct}\n# Wrong:{wrong}\nList to Study: {study}')

#stateCaps()

'''
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
'''

def encryptFile():    
    code = {'a': '!', 'A': '1', 'b': '@', 'B': '2', 'c': '#', 'C': '3', 'd' : '$','D' : '4', 'e' : '%',
            'E' :'5', 'f': '^', 'F': '6', 'g': '&', 'G': '7', 'h': '*', 'H': '8', 'i': '(', 'I': '9', 
            'j': ')', 'J': '0', 'k': 'Q', 'K': 'q', 'l': 'W', "L": 'w', 'm': 'E', "M" : 'e', "n": 'R',
            'N': 'r', 'o': 'T', 'O': 't', 'p': 'Y', 'P': 'y', 'q': 'U', 'Q': 'u', 'r':'I', 'R': 'i',
            's': 'O', 'S': 'o', 't': 'P', 'T':'p', 'u': 'A', 'U': 'a', 'v': 'S', 'V': 's', 'w': 'D',
            'W': 'd', 'x': 'F', 'X': 'f', 'y': 'G', 'Y': 'g', 'z': 'H', 'Z': 'h', '\n':'\n'}

    #open new 'encrypted' file
    e_file = open('encrypted.txt', 'w')

    #open document to be encrypted (as read)
    with open("document.txt") as f:
        # pull each line out
        for line in f:
            line.strip("\n")
            new_line = ''
            # pull each char out of the line
            for char in line:
                #get code value for the char and add to the string for a new line
                new_char = code[char]       #.rstrip("\n")
                new_line += new_char
            # write new line str to encrypted file
            e_file.write(new_line)
            print(new_line, end='')

    #ALWAYS CLOSE THE FILE
    e_file.close()

#encryptFile()

'''
4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
'''

def getUnique():
    unique = set()
    with open("unique.txt") as f:
        for line in f:
            fix = line.replace('\n', '')
            fix = fix.replace('.', '')
            fix = fix.replace(',', '')
            fix = fix.replace('(', '')
            fix = fix.replace(')', '')
            split = (fix.split(' '))
            if '' in split:
                split.remove('')
            new_list = []
            for word in split:
                new_list.append(word)
            unique.update(new_list)
            
    print(unique)
#import string
#for c in string.punctuation:
#...     s= s.replace(c,"")
#getUnique()



'''
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency
https://lipsum.com/
'''
def getWordFreq():
    word_freq = {}
    with open("unique2.txt") as f:
        for line in f:
            fix = line.replace('\n', '')
            fix = fix.replace('.', '')
            fix = fix.replace(',', '')
            fix = fix.replace('(', '')
            fix = fix.replace(')', '')
            split = (fix.split(' '))
            if '' in split:
                split.remove('')
            for word in split:
                lower = word.lower()
                if lower in word_freq:
                    word_freq[lower] += 1
                else:
                    word_freq[lower] = 1
    for key, value in word_freq.items():
        print(key, value, '\t', end='')

#getWordFreq()
'''
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.             XXX
• It should display a list of the words that appear in both files.             XXX
• It should display a list of the words that appear in the first file but not the second.             XXX
• It should display a list of the words that appear in the second file but not the first.             XXX
• It should display a list of the words that appear in either the first or second file but not both.             XXX
Hint: Use set operations to perform these analyses.
'''

def getCompareFiles():
    first = getSet('unique2.txt')
    second = getSet('compare2.txt')
    
    print(f'\nUnique words in unique2.txt: {first}')
    print(f'\nUnique words in compare.txt: {second}')
    print(f'\nWord in both files: {first & second}')                              #first.intersection(second)
    print(f'\nWords in first file (but not second): {first.difference(second)}')  #first - second
    print(f'\nWords in second file (but not first): {second.difference(first)}')  #second - first
    print(f'\nWords in either the first or second file but not both: {first ^ second}\n')   #

def getSet(p_file_name):
    my_set = set()
    with open(p_file_name) as f:
        for line in f:
            fix = line.replace('\n', '')
            fix = fix.replace('.', '')
            fix = fix.replace(',', '')
            fix = fix.replace('(', '')
            fix = fix.replace(')', '')
            split = (fix.split(' '))
            if '' in split:
                split.remove('')
            new_list = []
            for word in split:
                new_list.append(word)
            my_set.update(new_list)
    return my_set

#getCompareFiles()