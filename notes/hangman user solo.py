"""
Task:
    Your task is to implement the Hangman game in Python.
​
Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.
​
Assignment Notes:
If the letter has already been guessed, output a message to the player and ask for input again.

If the guess entered is not an alphabetic letter, output a message and ask for input again.
​
If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 

If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the player they have won and quit the game.
​
If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.
​
Bonus:
    You can do one or both of the following:
​
    1) Using a file:
    Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
    Read in the contents of the file and choose a word at random.
​
    2) Forever alone option:
    You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.
​
    3) Add some more functionality: 
        - Persist user profiles with scores
        - Prompt for which user is playing
        - Ask if the user wants to play a set of games
        - Build a leader board
        
    Have fun, get creative, and demonstrate what you've come up with.
"""

import string
import random
import pickle

def hangman():
    wrong_letters = []
    end = False
    profile_dict = getProfiles()
    getDisplay(profile_dict)
    user = 'computer'                                                # input('Enter your username: ')
    char_list = getCharList(getRandWord())                           # input('Have friend enter word: ')
    while len(wrong_letters) < 6 and end == False:    
        displayBlanks(char_list)
        char_list, wrong_letters = testGuess(char_list, wrong_letters)
        print(f"\nWrong Letters: {(', '.join(wrong_letters)).upper()}\nGuesses Left: {str(6-len(wrong_letters))}\n")
        # display win and get out of loop
        if ''.join(char_list).isupper():
            displayBlanks(char_list)
            print('You win!')
            end = True
    # check if max guess reached, display loss
    if len(wrong_letters) == 6:
        print(f"You Lose! The word was {''.join(char_list).upper()}")
        end = '1'
        print(end)
    updateProfile(user, 6-len(wrong_letters), profile_dict)   #6-len(wrong_letters) == score

def getProfiles():
    # get GAL from contacts.txt thru function
    profiles = {}
    # open in non closing way
    with open('profiles.txt', 'rb') as f:
        end_of_file = False
        # read to the end of the file
        while not end_of_file:
            try:
                # unpickle the next object
                profiles.update(pickle.load(f))
            except EOFError:
                # set the flag to indicate the end of the file has been reached
                end_of_file = True
    return profiles

def getDisplay(p_profiles):
    print('Description of Hangman and Rules\n')
    print('   Leader Board \n-------------------')
    for key, value in p_profiles.items():
        print(f'{key.title():^10} {value:^10}')
    print()

def updateProfile(p_user, p_score, p_profiles):
    if p_user in p_profiles.keys():
        p_profiles[p_user] += p_score
    else:
        p_profiles[p_user] = p_score
    with open('profiles.txt', 'wb') as out:
        # write changes to file in binary
        pickle.dump(p_profiles, out)

def getRandWord():
    with open('randhang.txt', 'r') as f:
        word_list = f.read()
    rand_word = random.choice(word_list.split('\n'))
    return rand_word

def getCharList(p_word):
    # loop thru word to create a char list
    letters = []
    for char in p_word.lower():
        letters += char
    return letters

def displayBlanks(p_word):
    #loop through the char list to display dashs, etc
    for value in p_word:
        if value.islower():
            print('_', end=" ")
        elif value.isupper() or value == ' ':
            print(value, end=" ")
    print()

def checkGuess(p_wrong):
    # error check the guess for letter and not guessed yet
    check = True
    while check == True:
        #guess = random.choice(list(string.ascii_lowercase))                                       #checkGuess(p_wrong)
        if guess in p_wrong:
            print(f"Already Guessed {guess.upper()}!")
        elif not(guess.isalpha()) or len(guess) != 1:
            print('You must enter a single letter (a-z)!')
        else:
            check = False
    return guess

def testGuess(p_word, p_wrong):
    # test each letter against guess and replace with uppercase if good guess
    guess = random.choice(list(string.ascii_lowercase))                                     #checkGuess(p_wrong)
    index = 0
    fails = 0
    print(f"The computer guessed {guess.upper()}")
    for char in p_word:
        if char == guess.lower():
            p_word[index] = char.upper()
        elif char == guess.upper():
            print(f'\nAlready Guessed: {guess.upper()}')
        else:
            fails += 1
        index += 1
    if fails == len(p_word):
        p_wrong.append(guess)
        print(f'\n{guess.upper()} was Wrong!')
    return p_word, p_wrong


hangman()