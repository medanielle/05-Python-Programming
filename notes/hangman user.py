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


import random
import pickle

def hangman():
    # initalize variables
    wrong_letters = []
    end = False
    profile_dict = getProfiles()
    # show leaderboard
    getDisplay(profile_dict)
    user = input('Enter your username: ')
    # get your word (either from user or word bank)
    char_list = list(getRandWord())                           # input('Have friend enter word: ')
    # loop until lose or win
    while len(wrong_letters) < 6 and end == False:
        # display board    
        displayBlanks(char_list)
        # get guess and test it
        char_list, wrong_letters = testGuess(char_list, wrong_letters)
        print(f"\nWrong Letters: {(', '.join(wrong_letters)).upper()}\n" \
            f"Guesses Left: {str(6-len(wrong_letters))}\n")
        # display win and get out of loop
        if ''.join(char_list).isupper():
            displayBlanks(char_list)
            print('You win!')
            end = True
    # check if max guess reached, display loss
    if len(wrong_letters) == 6:
        print(f"You Lose! The word was {''.join(char_list).upper()}")
    # update profile with user stats
    updateProfile(user, 6-len(wrong_letters), profile_dict)

# get profile dict from file with pickle
def getProfiles():
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

# show leaderboard
def getDisplay(p_profiles):
    print('Description of Hangman and Rules\n')
    print('   Leader Board \n-------------------')
    for key, value in p_profiles.items():
        print(f'{key.title():^10} {value:^10}')
    print()

# update profile dict with user and score
def updateProfile(p_user, p_score, p_profiles):
    # check if user already in the dict, then add points
    if p_user in p_profiles.keys():
        p_profiles[p_user] += p_score
    else:
        p_profiles[p_user] = p_score
    # write to file with pickle
    with open('profiles.txt', 'wb') as out:
        # write changes to file in binary
        pickle.dump(p_profiles, out)

# pull data from document and get random choice
def getRandWord():
    # open as read only
    with open('randhang.txt', 'r') as f:
        word_list = f.read()
    # pick random word/phrase
    rand_word = random.choice(word_list.split('\n'))
    # return the value
    return rand_word

# loop through the char list to display dashs, etc
def displayBlanks(p_word):
    # loop through char list and check each letter 
    for value in p_word:
        # if lower print an underscore
        if value.islower():
            print('_', end=" ")
        # if upper or space, print the letter
        elif value.isupper() or value == ' ':
            print(value, end=" ")
    print()

# error check the guess for letter and not guessed yet
def checkGuess(p_wrong):
    # intialize value for loop
    check = True
    while check == True:
        # get input letter from user
        guess = input('\nEnter a letter to guess: ')
        # check if it is in bad letter list
        if guess in p_wrong:
            print(f"Already Guessed {guess.upper()}!")
        # check if it is alpha or more than one
        elif not(guess.isalpha()) or len(guess) != 1:
            print('You must enter a single letter (a-z)!')
        # passed all test and end loop
        else:
            check = False
    # pass the guess variable on to Test
    return guess

# test each letter against guess and replace with uppercase if good guess
def testGuess(p_word, p_wrong):
    # use function to get and error check guess
    guess = checkGuess(p_wrong)
    # set up counting variables
    index = 0
    fails = 0
    # loop through each character in the string(list)
    for char in p_word:
        # lower = the original word; upper = the correct guesses
        if char == guess.lower():
            p_word[index] = char.upper()
        elif char == guess.upper():
            # error checks if they enter the same right answer twice
            print(f'\nAlready Guessed: {guess.upper()}')
        else:
            #tracks if all matches were wrong
            fails += 1
        # accumulator used to replace letter with correct guess
        index += 1
    #checks if each match was wrong
    if fails == len(p_word):
        # adds bad guess to wrong letter list
        p_wrong.append(guess)
        print(f'\n{guess.upper()} was Wrong!')
    #returns the char list and the bad letters
    return p_word, p_wrong


hangman()