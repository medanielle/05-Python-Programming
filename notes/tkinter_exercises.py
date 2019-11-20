"""

1. Name and Address
    Write a GUI program that displays your name and address when a button is clicked. 
    When the user clicks the Show Info button, the program should display your name and
    address. Mess with the display to make it look neat.

"""

import tkinter as tk

def my_info():
    # Window
    window = tk.Tk()
    window.title('My Info')
    window.geometry('400x400')

    def addr_display():
        # get greeting from phrase_generator
        addr = 'Danielle Hughett\n910 Rusting Cv\nSan Antonio, TX 78251'

        word_display = tk.Text(master= window, height=10, width=30)
        word_display.grid(column=0, row=2)

        word_display.insert(tk.END, addr)
        word_display.configure(state = 'disabled')   # now you can't type in our display box

    # Label
    label1 = tk.Label(text = 'My Name and Address')
    label1.grid(column=0, row=0)

    # Button define function before referenceing below (command =)
    button1 = tk.Button(text = "Click Me for The Info", command = addr_display)
    button1.grid(column=0, row=1, pady=(10,10))

    window.mainloop()

#my_info()

"""

2. Latin Translator
    Look at the following list of Latin words and their meanings.
        Latin       English
        sinister    left
        dexter      right
        medium      center
    Write a GUI program that translates the Latin words to English. The window should have
    three buttons, one for each Latin word. When the user clicks a button, the program displays 
    the English translation in a label.

"""
def gui_latin():
    my_dict = {'sinister': 'left', 'dexter': 'right', 'medium': 'center'}

    # Window
    window = tk.Tk()
    window.title('Latin Translator')
    window.geometry('400x400')

    def word_display(my_str, r):
        # get greeting from phrase_generator
        english = my_dict[my_str]

        english_display = tk.Text(master=window, height=1, width=10)
        english_display.grid(column=1, row=r, pady=(10,0))

        english_display.insert(tk.END, english)
        english_display.configure(state = 'disabled')   # now you can't type in our display box

    # Label
    label1 = tk.Label(text = 'Click the word for English translation')
    label1.grid(column=0, row=0)

    label2 = tk.Label(text = 'Latin')
    label2.grid(column=0, row=1, pady=(10,0))

    label3 = tk.Label(text = 'English')
    label3.grid(column=1, row=1, pady=(10,0))


    # Buttons
    #frame1= tk.Frame()
    #frame1.grid(column=0, row=2, columnspan=3)
    button1 = tk.Button(text = 'sinister', command = lambda: word_display('sinister', 2))
    button1.grid(column=0, row=2, pady=(10,0))

    button2 = tk.Button(text = 'dexter', command = lambda: word_display('dexter', 3))
    button2.grid(column=0, row=3, pady=(10,0))

    button3 = tk.Button(text = 'medium', command = lambda: word_display('medium', 4))
    button3.grid(column=0, row=4, pady=(10,0))

    window.mainloop()

#gui_latin()

"""
3. Miles Per Gallon Calculator
    Write a GUI program that calculates a car’s gas mileage. The program’s window should
    have Entry widgets that let the user enter the number of gallons of gas the car holds, and
    the number of miles it can be driven on a full tank. When a Calculate MPG button is
    clicked, the program should display the number of miles that the car may be driven per gallon of gas. 
    Use the following formula to calculate miles-per-gallon:

        MPG = miles/gallons

"""

def gui_mpg():
    # Window
    window = tk.Tk()
    window.title('MPG')
    window.geometry('400x400')

    def mpg_display():
        # get greeting from phrase_generator
        my_mpg = str(f'Your MPG is {(float(miles.get())/float(gallons.get()))} miles/gallon.')
        print(my_mpg)
        num_display = tk.Text(master=window, height=1, width=30)
        num_display.grid(column=0, row=4, pady=(10,0), columnspan =2)

        num_display.insert(tk.END, my_mpg)
        num_display.configure(state = 'disabled')   # now you can't type in our display box

    # Label
    label1 = tk.Label(text = 'Enter your Miles and Gallons per Full Tank')
    label1.grid(column=0, row=0, columnspan=2)

    label2 = tk.Label(text = 'Miles')
    label2.grid(column=0, row=1, pady=(10,0))

    label3 = tk.Label(text = 'Gallons')
    label3.grid(column=0, row=2, pady=(10,0))

    # Entry
    miles = tk.Entry()
    miles.grid(column=1, row=1, padx=(30,0), pady=(10,0))

    gallons = tk.Entry()
    gallons.grid(column=1, row=2, padx=(30,0), pady=(10,0))

    # Buttons
    button1 = tk.Button(text = 'Click to calculate MPGs', command = mpg_display)
    button1.grid(column=0, row=3, pady=(10,0), columnspan=2)

    window.mainloop()

#gui_mpg()
"""

4. Celsius to Fahrenheit
    Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. The user
    should be able to enter a Celsius temperature, click a button, and then see the equivalent
    Fahrenheit temperature. Use the following formula to make the conversion:

        F = (9/5)C + 32

    F is the Fahrenheit temperature and C is the Celsius temperature.
"""

def gui_cel_fah():
    # Window
    window = tk.Tk()
    window.title('Celsius to Fahrenheit Converter')
    window.geometry('400x400')

    def fah_display():
        # get greeting from phrase_generator
        my_fah = str(f'Fahrenheit = {((9/5)*float(cel.get())+32)}')
        print(my_fah)
        fah_display = tk.Text(master=window, height=1, width=20)
        fah_display.grid(column=0, row=4, pady=(10,0), sticky = 'nsew')

        fah_display.insert(tk.END, my_fah)
        fah_display.configure(state = 'disabled')   # now you can't type in our display box

    # Label
    label1 = tk.Label(text = 'Celsius to Fahrenheit Converter')
    label1.grid(column=0, row=0, sticky = 'nsew')

    label2 = tk.Label(text = 'Enter the degrees Celcius: ')
    label2.grid(column=0, row=1, pady=(10,0), sticky = 'nsew')

    # Entry
    cel = tk.Entry()
    cel.grid(column=0, row=2, padx=(30,0), pady=(10,0))

    # Buttons
    button1 = tk.Button(text = 'Click for degrees Fahrenheit', command = fah_display)
    button1.grid(column=0, row=3, pady=(10,0))

    window.mainloop()

#gui_cel_fah()

"""
5. Property Tax
    A county collects property taxes on the assessment value of property, which is 60 percent
    of the property’s actual value. If an acre of land is valued at $10,000, its assessment value
    is $6,000. The property tax is then $0.64 for each $100 of the assessment value. The tax
    for the acre assessed at $6,000 will be $38.40. Write a GUI program that displays the
    assessment value and property tax when a user enters the actual value of a property.
"""
def gui_prop_tax():

    # Window
    window = tk.Tk()
    window.title('Property Tax Calculator')
    window.geometry('400x400')

    #def getCountyPropTax(p_value):
        #propTax = p_value * .6 * .0064
        #return propTax

    def tax_display():
        # get greeting from phrase_generator
        my_tax = str(f'Property Tax = ${(float(value.get()) * .6 * .0064):.2f}')
        print(my_tax)
        tax_label = tk.Label(text = my_tax)
        tax_label.grid(column=0, row=4, pady=(10,0))

    # Label
    label1 = tk.Label(text = 'Property Tax Calculator')
    label1.grid(column=0, row=0, sticky = 'nsew')

    label2 = tk.Label(text = 'Enter the property value: ')
    label2.grid(column=0, row=1, pady=(10,0), sticky = 'nsew')

    # Entry
    value = tk.Entry()
    value.grid(column=0, row=2, pady=(10,0))

    # Buttons
    button1 = tk.Button(text = 'Click for Property Tax', command = tax_display)
    button1.grid(column=0, row=3, pady=(10,0))

    window.mainloop()

#gui_prop_tax()


"""
6. Joe’s Automotive
    Joe’s Automotive performs the following routine maintenance services:
        • Oil change          —   $26.00
        • Lube job            —   $18.00
        • Radiator flush      —   $30.00
        • Transmission flush  —   $80.00
        • Inspection          —   $15.00
        • Muffler replacement —   $100.00
        • Tire rotation       —   $20.00
    Write a GUI program with check buttons that allow the user to select any or all of these
    services. When the user clicks a button the total charges should be displayed.

"""
from tkinter import IntVar
from tkinter import ttk

def gui_auto_cart():

    # Window
    window = tk.Tk()
    window.title('Joe’s Automotive')
    window.geometry('400x400')

    my_dict = {'Oil change          —   $26.00': 26.00, 'Lube job            —   $18.00': 18.00,            'Radiator flush      —   $30.00': 30.00, 'Transmission flush  —   $80.00': 80.00,             'Inspection          —   $15.00': 15.00, 'Muffler replacement —   $100.00': 100.00,           'Tire rotation       —   $20.00': 20.00}

    # Label
    label1 = tk.Label(text = 'Joe’s Automotive')
    label1.grid(column=0, row=0, sticky = 'nsew')

    label2 = tk.Label(text = 'Choose your services: ')
    label2.grid(column=0, row=1, pady=(10,0))

    #count = 2
    v = IntVar()
    v.set(0) # initialize
    count = 2
    for key, value in my_dict.items():
        b = tk.Radiobutton(text=key, variable=v, value=value)
        b.grid(column=0, row=1, pady=(10,0))
        count += 1
        #radio1 = tk.Radiobutton(master=window, text=key, sticky= 'w', padx=(20,0))
        #radio1.grid(column=0, row=count)
        #count += 1

    # Buttons
    button1 = tk.Button(text = 'Get Total') #command = total_display)
    button1.grid(column=0, row=2+count, pady=(10,0))

    window.mainloop()

gui_auto_cart()



"""
for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
"""