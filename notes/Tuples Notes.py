def first():
    #tuples

    #initalize a tuple

    my_tuple = (1, 2, 3, 4, 5)

    print(my_tuple)

    #printing items in a tuple
    names = ('Holly', 'Warren', 'Ashley')

    for n in names:
        print(n)

    for i in range(len(names)):
        print(i)
        print(names[i])

#tuples are immutable

#first()

def getTupleFromList():
    mylist = [2, 4, 5, 1, 6]
    type(mylist)                #<class 'list'>
    tuple(mylist)               #(2, 4, 5, 1, 6)
    mytuple = tuple(mylist)
    type(mylist)                #<class 'list'>
    type(mytuple)               #<class 'tuple'>

#getTupleFromList

