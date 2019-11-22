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
from functools import partial

def chunn_latin():
    # Instantiate the window
    window = tk.Tk()

    # set the window geometry and title
    window.geometry('400x400')
    window.title('Latin Translator')

    # define the function to show the info
    def display_English(p_latin):
        # def blank labels to generate from for the dictionary
        labelLeft = None
        labelRight = None
        labelCenter = None
        # Define a translation dictionary with the Latin words as a key
        translation = {
            'sinister' : {'English': 'left', 'label' : labelLeft, 'col' : 0},
            'dexter' : {'English': 'right', 'label' : labelRight, 'col' : 2},
            'medium' : {'English': 'center', 'label' : labelCenter, 'col' : 1}
        }
        # prepare the label to display
        translation[p_latin]['label'] = tk.Label(master=window, text=translation[p_latin]['English'])
        translation[p_latin]['label'].grid(column=translation[p_latin]['col'], row=3)

    # build a title header label for the window
    titleLatin = tk.Label(text='Latin')
    titleLatin.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
    titleEnglish = tk.Label(text='English')
    titleEnglish.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

    # Build the buttons that calls the display translation function when clicked
    buttonleft = tk.Button(text='sinister', command=partial(display_English, 'sinister'))
    buttonleft.grid(column=0, row=1, padx=10, pady=10)
    buttoncenter = tk.Button(text='medium', command=partial(display_English, 'medium'))
    buttoncenter.grid(column=1, row=1, padx=10, pady=10)
    buttonright = tk.Button(text='dexter', command=partial(display_English, 'dexter'))
    buttonright.grid(column=2, row=1, padx=10, pady=10)


    # call the window mainloop function
    window.mainloop()

# Call the main function
chunn_latin()
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
        #print(my_mpg)
        num_display = tk.Label(master=window, text=my_mpg)
        num_display.grid(column=0, row=4, pady=(10,0), columnspan =2)

        # num_display.insert(tk.END, my_mpg)
        # num_display.configure(state = 'disabled')   # now you can't type in our display box

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

gui_mpg()
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
#from tkinter import ttk

def gui_auto_cart():
    # intialize accumulator variable, and dictionary for menu items
    total_list = []
    my_dict = {'Oil change          —   $26.00': 26.00, 'Lube job            —   $18.00': 18.00,            'Radiator flush      —   $30.00': 30.00, 'Transmission flush  —   $80.00': 80.00,             'Inspection          —   $15.00': 15.00, 'Muffler replacement —   $100.00': 100.00,           'Tire rotation       —   $20.00': 20.00}
     
    # Window
    window = tk.Tk()
    window.title('Joe’s Automotive')
    window.geometry('360x400')

    # Label
    label1 = tk.Label(text = 'Joe’s Automotive')
    label1.grid(column=0, row=0, padx=(50,0))

    label2 = tk.Label(text = 'Choose your services: ')
    label2.grid(column=0, row=1, pady=(10,0), padx=(50,0))

    # function for displaying the radio buttons
    def display_radio():
        # for loop goes through a counter(starting at 2) for row, and my dict(item = key)
        for row, item in enumerate(my_dict, 2):
            label = tk.Label(window, text=item)
            label.grid(row=row, column = 0, padx=(50,0))
            var = tk.IntVar()
            var.set(0)
            button = tk.Radiobutton(window, variable = var, value = my_dict[item]) 
            button.grid(row = row, column = 1, padx=(50,0))
            total_list.append(var)

    # this function calculates total from list and calls the display function
    def get_total():
        total = 0
        for v in total_list:
            total += v.get()
        show_total(float(total))

    # function creates label for total to be printed
    def show_total(p_total):
        label3 = tk.Label(text= f'Your Total is ${p_total:.2f}')
        label3.grid(column=0, row = 11, pady=(20,0), padx=(50,0))
        return label3
        
    # this function clears the total accumulator, and then re-displays the buttons
    def get_reset():
        total_list.clear()
        display_radio()
        get_total()
        

    display_radio()

    # Buttons
    button1 = tk.Button(text = 'Get Total', command = get_total)
    button1.grid(column=0, row=10, pady=(20,0), padx=(50,0))

    button2 = tk.Button(text = 'Reset Selections', command = get_reset)
    button2.grid(column=0, row=12, pady=(20,0), padx=(50,0))

    window.mainloop()

#gui_auto_cart()
def chunn_auto():
    # instantiate the window
    window = tk.Tk()

    # Set the window title and geometry (As Desired)
    window.title('Joe\'s Automotive')
    # window.geometry('400x400')

    # Create the checkbuttons and variables
    var_oil = tk.BooleanVar()
    var_lube = tk.BooleanVar()
    var_radiator = tk.BooleanVar()
    var_transmission = tk.BooleanVar()
    var_inspection = tk.BooleanVar()
    var_muffler = tk.BooleanVar()
    var_tire_rot = tk.BooleanVar()
    var_total = tk.StringVar()
    var_total.set(0.00)
    final_row = 0

    jobs_dict = {
        'Oil Change:' : {'cost' : 26.00, 'ck_var': var_oil},
        'Lube Job:' : {'cost' : 18.00, 'ck_var': var_lube},
        'Radiator Flush:' : {'cost' : 30.00, 'ck_var': var_radiator},
        'Transmission Flush:' : {'cost' : 80.00, 'ck_var': var_transmission},
        'Inspection:' : {'cost' : 15.00, 'ck_var': var_inspection},
        'Muffler Replacement:' : {'cost' : 100.00, 'ck_var': var_muffler},
        'Tire Rotation:' : {'cost' : 20.00, 'ck_var': var_tire_rot}
    }

    # define the total function
    def calc_total():
        # initialize a total accumalator
        total = 0
        # Iterate through all possible jobs
        for job in jobs_dict.keys():
            # if job's checkbutton variable is set to 1
            if jobs_dict[job]['ck_var'].get() == 1:
                # add the job's cost to the total
                total += jobs_dict[job]['cost']
        # set the total vaiable to the total
        var_total.set(f'Total:\t${total:.2f}')
    
    # create an empty list to store all of the created checkbuttons
    all_checkbuttons = []

    # Create a checkbutton for each job
    for job in jobs_dict.keys():
        if len(job) > 15:
            checkbutton = tk.Checkbutton(text='{} \t${:.2f}'.format(job, jobs_dict[job]['cost']), variable=jobs_dict[job]['ck_var'], onvalue=1, offvalue=0, width=30, command=calc_total, anchor='w')
        else:
            checkbutton = tk.Checkbutton(text='{} \t\t${:.2f}'.format(job, jobs_dict[job]['cost']), variable=jobs_dict[job]['ck_var'], onvalue=1, offvalue=0, width=30, command=calc_total, anchor='w')
        all_checkbuttons.append(checkbutton)

    # place the checkbuttons on the gui grid and configure as necessary
    for r, button in enumerate(all_checkbuttons):
        button.grid(row=r, column=0, padx=5)
        final_row = r + 1

    # create the total label
    label_total = tk.Label(textvariable=var_total)
    label_total.grid(row=final_row, column=0)

    # call the window mainloop
    window.mainloop()
# Call the main function
chunn_auto()
