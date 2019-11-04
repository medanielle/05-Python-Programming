def writeThreeLines():
    #demo write 3 lines of text to a file
    
    f = open('philo.txt', 'w')
    #if you use full path r'path' to escape the \s

    #write names of three philo
    f.write('John Locke\n')
    f.write('David Hume\n')
    f.write('Edmund Burke\n')

    #ALWAYS CLOSE FILE
    f.close()

    # it was saved here 'C:\Users\student\Documents\05-Python-Programming'

#writeThreeLines()

def readDisplayFile():
    #demos reading and displaying the philo.txt file
    #opens file in read mode
    f = open('philo.txt', 'r')

    # read file contents
    f_contents = f.read()

    #ALWAYS CLOSE FILE
    f.close()

    #print the data the was read into memory
    print(f_contents)

#readDisplayFile()

def oneLineAtATime():
    #demos read contents of philo.txt 1 line at a time
    #open file in read only
    f =open('philo.txt', 'r')

    #read one line
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    # or combine with above line1 = f.readline().rstrip('\n')
    #strip the new line from each string
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    #ALWAYS CLOSE FILE
    f.close()

    #print the data the was read into memory
    #print(line1, end='')  click on line => alt + next line => keep holding alt + next line 
    #Ctrl + Alt + arrow
    print(line1 + line2 + line3)

#oneLineAtATime()

def getAppending():
    #append to philo.txt
    f = open('philo.txt', 'a')

    #write our append to the file 
    f.write('Danielle Hughett\n')

    #ALWAYS CLOSE FILE
    f.close()

#getAppending()

def getSalesTxt():
    #create new file with
    f = open('sales.txt', 'w')

    #write our append to the file 
    f.write('1000.0\n2000.0\n3000.0\n4000.0\n')

    #ALWAYS CLOSE FILE
    f.close()

#getnewex()

def createAndWrite():
    #demos prompting user for sales amounts and write those amounts to the sales2.txt
    #get number of days
    num_days = int(input('Enter number of days of sales: '))

    #open a new file names sale2.txt
    sales_file = open('sales2.txt', 'w')

    #get amount of sales for each day and write to file
    for count in range(1, num_days+1):
        #get sales for the day
        sales = float(input(f'Enter the sales for day #{str(count)}: '))
            # or ('enter #' + \ 
            # str(count) + ': "")
        sales_file.write(str(sales) + '\n')

    #ALWAYS CLOSE THE FILE
    sales_file.close()
    print('Data written to sales2.txt')

#createAndWrite()

def newReadEx():
    #demo read all values in sales2.txt
    #open file for reading
    sales_file = open('sales2.txt', 'r')

    #read the first linefrom the file, but don't convert to a number yet
    #neeed to test an empty string
    line = sales_file.readline()

    #as long as an empty string is not returned from readline, continue processing
    while line != '':
        #convert to a float
        amount = float(line)

        #format and display
        print(format(amount, '.2f'))

        #read the next line
        line = sales_file.readline()
    
    #ALWAYS CLOSE THE FILE
    sales_file.close()

#newReadEx()


def newDisplay():
    #demo displaying contents of file
    try:    
        #get name of file
        filename = input('Enter file name: ')

        #open the file
        infile = open(filename, 'r')

        #read contents
        contents = infile.read()
        
        #display contents
        print(contents)

        #ALWAYS CLOSE FILE
        infile.close
    
    except IOError:
        print('An error occured trying to read the file:', filename)

#newDisplay()

def withoutClose():
    with open('sales2.txt', 'r') as filer:
        #contents = filer.read()
        #print(contents)
        for line in filer:
            print(line, end ='')

#withoutClose()

def withoutCloseTWO():
    with open('philo.txt', 'r') as filer:
        size_to_read = 10
        f_contents = filer.read(size_to_read)
        #print(f_contents)

        while len(f_contents) > 0:
            print(f_contents, end='-')
            f_contents = filer.read(size_to_read)

withoutCloseTWO()
    

#def firstExample():
    #file_variable = open(filename, mode)
        #f = open('file.txt', 'r')