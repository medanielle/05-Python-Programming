def first():
    #list syntax of even numbers
    even_number = [2, 4, 6, 8, 10]
    print(even_number)

    #list of strings
    names = ['Hydrick', 'George', 'Ali', 'Howard']

    #list con hold different types
    diff_types_list = ['Chunn', 100, False, 3.14]

    #show items in list
    print(diff_types_list)

    #using rang in a list
    range_list = list(range(1, 10, 2))
    print(range_list)

    #repitition operator
    #list * n
    name = names[0] * 5
    print(name)

    #print numbers list mulitple times
    numbers = [1, 2, 3] * 3
    print(numbers)

    #loop over list
    large_nums = [99, 100, 101, 2000000]
    for n in large_nums:
        print(n)
    
    #indexing with a list
    my_list = [10, 20, 30, 40, 50]
    print(my_list[2])  #30
    print(my_list[-4])  #20

    # loop for len(list)
    #find length of list
    len_list = len(my_list)
    print(len_list)

    #lists are mutable
    print(large_nums)
    large_nums[1] = 1337
    print(large_nums)

#first()

def second():
    #syntax for slicing
    #list_name[start:end]

    #slice list example
    days = ['Sunday', 'Monday', 'tuesday', 'wednesday', 'Thursday', 'friday', 'saturday']
    mid_days = days[2:5]
    print(mid_days)
    #['tuesday', 'wednesday', 'Thursday']

    numbers = [1,2,3,4,5]
    print(numbers[:3])
    #[1, 2, 3]

    print(numbers[2:])
    #[3, 4, 5]

    print(numbers[:]) #colon is redunundant and unnecasry 
    #[1, 2, 3, 4, 5]

#second()

def third():
    #finding items in list 
    #item in list
    numbers = [1,2,3,4,5]
    print(4 in numbers)
    #True

    #item not in list
    print(4 not in numbers)
    #False

    print(6 not in numbers)
    #True

#third()

def functionality():
    #builtin functionality for lists

    #append
    def appending():
        #initalize empty list
        name_list = []

        #Create variable to control out loop
        again = 'y'

        # add some names to a list
        while again == 'y':
            #get name from user
            name = input('Enter a name: ')

            #append it to the list
            name_list.append(name)

            #add another?
            print('Do you want to add another name?')
            again = input('y = yes, anything else = no: ')
            print()

        print('Here are the names you entered:')

        for name in name_list:
            print(name)
        
    #appending()

    def getIndex():
        #demos the index of an item ina  list and then replace that item w/ a new item

        #create a list w/some items
        food = ["pizza", 'burgers', 'chips']

        #display the list
        print('Here are the items in the food list')
        print(food)

        #get item to change
        item = input("Which item should i change? ")

        try:
            #get item index in the list
            item_index = food.index(item)

            #get value to replace with from user
            new_item = input('Enter the new: ')

            #replace old item with new item
            food[item_index] = new_item

            #display the list
            print('here is the revised list: ')
            print(food)
        
        except ValueError:
            #user entered something not in our list
            print('That item was not found in the list!')
    #getIndex()


    #demo the insert method
    def getInsert():
        #create a list
        names = ['James', 'Kathryn', 'Bill']

        #display the list
        print('This is the list before insert: ')
        print(names)

        #insert a new name at element 0
        names.insert(0, 'Joe')

        #display the list
        print('This is the list after insert: ')
        print(names)

    #getInsert()

    def getSort():
        #out of order list
        my_list = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]

        #display unsorted
        print('Original order: ', my_list)

        # changes it permanently vs sorted()
        my_list.sort()

        print('Sorted order: ', my_list)

        ####new one with sorted()
        #out of order list
        my_list2 = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]

        #display unsorted
        print('Original order: ', my_list2)

        # changes it permanently vs .sorted()
        print(sorted(my_list2))

        print('Sorted order: ', my_list2)

        #in reverse sort
        my_list.sort(reverse=True)

        #printed in reverse sort
        print('Reverse Sorted order: ', my_list)


    #getSort()

    def getRemove():
        #demos the remove from list method
        #create a list w/some items
        food = ["pizza", 'burgers', 'chips']

        #display the list
        print('Here are the items in the food list')
        print(food)

        #get item to change
        item = input("Which item should i change? ")

        try:
            #remove the item
            food.remove(item)

            #display the list
            print('here is the revised list: ')
            print(food)
        
        except ValueError:
            print('not in list!')
    #getRemove()

    def getReverse():
        #reverse method
        #initalize list
        my_list = [1, 2, 3, 4, 5]
        print('original order: ', my_list)

        my_list.reverse()
        print('Reversed: ', my_list)
    #getReverse()

    def getDelete():
        #used with element #(index) nrather than item to search
        #initalize list
        my_list = [1, 2, 3, 4, 5]
        print('Before deletion: ', my_list)

        #del statement
        del my_list[2:4]
        print('After deletion: ', my_list)
    #getDelete()

    def getMinOrMax():
        #demos min and max functiosn
        #intialize list
        mylist = [5, 4, 3, 2, 50, 40, 30]
        #mylist2 = ['Amanda', 'amand', 'amanda']
        #ord('A') =65; ord('a') = 97; ord('z') = 122; ord('Z') 90

        #find the minimum value
        print('The lowest value is ', min(mylist))

        #find the maximum value
        print('THe highest value is ', max(mylist))
    
    #getMinOrMax()

    def getCopy():
        #copying list in python

        #create a list
        list1 = [1, 2, 3, 4]

        #assining to list2 variable
        list2 = list1

        #display the list
        print(list1)                #[1, 2, 3, 4]
        print(list2)                #[1, 2, 3, 4]

        #replace part of the list
        list1[0] = 99                #same for list2[0] = 99
        print(list1)                 #[99, 2, 3, 4]
        print(list2)                 #[99, 2, 3, 4]

        #points to memory space, not just the straight data
        #how to copy two separate but identical lists
        list3 = [1, 2, 3, 4]

        #create empty list
        list4 = []

        #display lists
        print('original list3 ',list3)
        print('original list4 ',list4)

        # copy the elelments one by one
        for item in list3:
            list4.append(item)
        
        
        # or this way with out for loop
        # list4 = list3.copy()

        print('orig appended  list4 ',list4)

        #replace to test
        list3[0] = 99
        print('final list3 ',list3)
        print('final list4 ',list4)
    
    #getCopy()

    def getArgument():
        #demos function to calc total values in a list

        #create a list
        numbers = [2, 4, 6, 8, 10]

        # Display total of list elements
        print('The total is', get_total(numbers))

    def get_total(value_list):
        #create accumulator
        total = 0

        #calc the total
        for num in value_list:
            total += num
        
        #return total
        return total

    #getArgument()

    def getListToFile():
        #demo uses writelines to save a list of strings to a file
        #must add \n if you want new lines between each
        cities = ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']

        #open file for writing
        outfile = open('cities.txt', 'w')

        #write lines to the file
        outfile.writelines(cities)
        
        #ALWAYS CLOSE
        outfile.close()
    
    #getListToFile()

    def getListToFile2():
        #demo uses a loop with write to save a list of strings to a file
        #must add \n if you want new lines between each
        cities = ['New York\n', 'Boston\n', 'Atlanta\n', 'Dallas\n']

        #open file for writing
        outfile = open('cities.txt', 'w')

        #write lines to the file with loop
        for item in cities:
            outfile.write(item)
        
        #ALWAYS CLOSE
        outfile.close()
    
    #getListToFile2()

    def getFileToList():
        #demo uses writelines to save a list of strings to a file

        #open file for writing
        infile = open('cities.txt', 'r')

        #read lines from the file    ##MUST BE READLINES() because of removing the \n
        cities_read_in = infile.readlines()
                
        #ALWAYS CLOSE
        infile.close()
    
        index = 0
        while index < len(cities_read_in):
            cities_read_in[index] = cities_read_in[index].rstrip('\n')
            index += 1

        #print the contents of the list
        print(cities_read_in)
    #getFileToList()

    def getTwoDimensional():

        students = [ ['joe', 'kim'], ['sam', 'sue'], ['kelly', 'christ']]
        print(students)                      #[['joe', 'kim'], ['sam', 'sue'], ['kelly', 'christ']]

        print(students[0])                  #['joe', 'kim']

        print(students[0][0])                  #joe

        print('I want to print Sue', students[1][1])             #I want to print Sue sue

    #getTwoDimensional()

    def getRandList():
        import random

        #constants fro rows and columns
        ROWS = 3
        COLUMNS = 4

        def createList():
            #create two dimensinal list
            values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

            for r in range(ROWS):
                row_total = 0
                for c in range(COLUMNS):
                    values[r][c] = random.randint(0, 1)
            print(values)

        createList()
    getRandList()

    #.extend() == concatinate another list or iterables

functionality()