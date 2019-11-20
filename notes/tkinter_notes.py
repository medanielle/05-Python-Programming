# Documentation:  effbot.org/tkinterbook/text.html
# 
# GUI - graphical user interface allows the user to interact with the OS and other programs using graphical elements such as icons, buttons, and dialog boxes

# In Python, you can use the tkinter module to create simple GUI programs

# THere are other modules available but tkinter comes with Python

# ******************** tkinter widgets **********************

# Button - A button that can cause an action to occur when it is clicked
# Canvas - A rectangle area that can be used to display graphics
# Checkbutton - A button that may be  in either the 'on' or 'off' position
# Entry - An Area in which the user may type a single line of input from keyboard
# Frame - a container that can hold other widgets
# Label - An area that displays one line of text or an image
# Listbox - A list from which the user ,au select an item
# Menu - A list of menu choices that are displayed when the user clicks a Menubutton widget
# Menubotton - A menu that is displayed on the screen and may be clicked by the user
# Radiobutton - A widget that can be either selected or deselected. Can choose one option in a group
# Scale - A widget that allows the user to select a value by moving a slider along a track
# Scrollbar - Can be used with some other types of widgets to provide scrolling capabilities
# Text - A widget that allows the user to enter multiple lines of text input
# Toplevel - A container, like a Frame, but displayed in its own window


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Access tkinter
import tkinter as tk

def tkinter_window():
    # instantiate a tkinter object
    window = tk.Tk()

    # set title for window
    window.title('First tkinter app')

    # set the size of your window (so it won't be small, baby window)
    window.geometry('500x500')

    # Adding a Label
    title = tk.Label(text = 'Hello World! This font is better', font = ("Times New Roman", 24))
    
    # grid() tells you where you want the label, (0,0) is default
    title.grid(column=0, row= 0, pady=(0, 10))   # specific location
    #title.pack()    # just shove it in there, wherever they fit

    # Add a Button
    button1 = tk.Button(text = 'Click Me', bg='red')  # bg = background color
    button1.grid(column=0, row= 1)  # you don't have to be specific default will adjust

    # Adding an Entry
    entry_field1 = tk.Entry()
    entry_field1.grid(column=0, row=2, pady=(10, 10))

    # adding a Text Field (multi-line input)
    text_field = tk.Text(master = window, height = 10, width=30)
    text_field.grid(column=0, row=3)


    # this opens your window, this is like calling your function. Everything you do must be between this and instantiating your window
    # this is always at the bottom
    # Continuously puts the window in a loop to keep it open
    window.mainloop()
#tkinter_window()


import tkinter as tk
import random

def salutations_app():
    # Window
    window = tk.Tk()
    window.title('Salutations')
    window.geometry('400x400')

    def phrase_gen():
        # Create list of Phrases
        phrases = ['Hello ', "What's up ", 'Howdy ', 'Aloha ']
        # get name from entry field
        name = str(entry_field1.get())

        return random.choice(phrases) + name + '!'

    def phrase_display():
        # get greeting from phrase_generator
        greeting = phrase_gen()

        greeting_display = tk.Text(master= window, height=10, width=30)
        greeting_display.grid(column=0, row=3)

        greeting_display.insert(tk.END, greeting)
        greeting_display.configure(state = 'disabled')   # now you can't type in our display box

    # Label
    label1 = tk.Label(text = 'How you doin...')
    label1.grid(column=0, row=0)

    label2 = tk.Label(text = 'What is your name?')
    label2.grid(column=0, row=1)

    #Entry
    # no arguments because we want to take user input

    entry_field1 = tk.Entry()
    entry_field1.grid(column=1, row=1, padx=(30,0))

    # Button define function before referenceing below (command =)
    button1 = tk.Button(text = "Click Me!", command = phrase_display)
    button1.grid(column=0, row=2)


    window.mainloop()

salutations_app()


