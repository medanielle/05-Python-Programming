"""
1. 
    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter 
    a filename and a string to be removed.

    Points Of Authority - Linkin Park

Forfeit the game
Before somebody else
Takes you out of the frame
And puts your name to shame
Cover up your face
You can't run the race
The pace is too fast
You just won't last

You love the way I look at you
While taking pleasure in the awful things you put me through
You take away if I give in
My life, my pride is broken

You like to think you're never wrong
(You live what you've learned)
You have to act like you're someone
(You live what you've learned)
You want someone to hurt like you
(You live what you've learned)
You want to share what you've been through
(You live what you've learned)

You love the things I say I'll do
The way I'll hurt myself again just to get back at you
You take away when I give in
My life, my pride is broken

You like to think you're never wrong
(You live what you've learned)
You have to act like you're someone
(You live what you've learned)
You want someone to hurt like you
(You live what you've learned)
You want to share what you've been through
(You live what you've learned)

Forfeit the game
Before somebody else
Takes you out of the frame
And puts your name to shame
Cover up your face
You can't run the race
The pace is too fast
You just won't last

Forfeit the game
Before somebody else
Takes you out of the frame
And puts your name to shame
Cover up your face
You can't run the race
The pace is too fast
You just won't last

You like to think you're never wrong
(You live what you've learned)
You have to act like you're someone
(You live what you've learned)
You want someone to hurt like you
(You live what you've learned)
You want to share what you've been through
(You live what you've learned)
        """
# function to read file and create a list of lines
# parameters: p_my_path = file path inputed by user in main
def read_original(p_my_path):
    # open file
    with open(p_my_path, 'r') as f:
        # use readlines() to get an iterable with the list of strings/lines
        lyrics = f.readlines()
    return lyrics

# function to search and remove the string from each line
# parameters: p_lyrics = original file's info (as list of each line as a string),
#             p_my_str = string user entererd in main
def remove_text(p_lyrics, p_my_str):
    # intialize the new variable to hold your list of lines
    new_lyrics = []
    # go through each line in the file
    for line in p_lyrics:
        # check if the string is in that line
        if p_my_str in line:
            #if the string is found, then strip the string from the line, and add to the new list of lines
            new_lyrics.append(line.replace(p_my_str, ''))
        else:
            # keep line as is and add to the new list of lines
            new_lyrics.append(line)
    return new_lyrics

# function to print my new list of lines to a new document
# paramenters: p_out_path = where to save the file, 
#              p_filtered = list of lines to write to the file
def write_filtered(p_out_path, p_filtered):
    # open file
    with open(p_out_path, 'w') as f:
        # use writelines to write an iterable
        f.writelines(p_filtered)
        
def main():
    my_path = input('Enter the text file (and path to search): ')
    #my_str = 'Take'
    my_str = input('Enter the string to search for and remove: ')
    # call the read function to get list of lines orgianlly in that path provided
    my_original = read_original(my_path)
    # set variable to the list of lines that have string removed from them (send the str, and path for file)
    filtered = remove_text(my_original, my_str)
    # change filepath to add new to end
    out_path = my_path.replace('.txt', '_new.txt')
    # send list of lines and new out path to the write lines function
    write_filtered(out_path, filtered)
    

# call main
main()