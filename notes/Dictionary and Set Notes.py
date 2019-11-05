#Dictionary
# A Dictionary is an object that stores a collection of data. Each elelment in a dictionary has two parts: a key and a value. you use a key to locate a specific value

def first():
    # creating a dictionary
    phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
    print('\n', phonebook)

    # print pretty?
    for item in phonebook.keys():
        print('\n', item, ':', phonebook[item])

    #retrieve a value from a dictionary
    print('\n', phonebook['Katie'])

    # using the in and not in operators to test for a value
    if 'Chris' in phonebook:
        print(phonebook['Chris'])

    if 'David' not in phonebook:
        print('Not in phone book')

    # adding an element
    phonebook['David'] = '555-4444'
    print('\n', phonebook)

    # Remove an element
    del phonebook['David']
    print('\n', phonebook)

    # finding length of dict
    length_dict = len(phonebook)
    print('\n', length_dict)

    # Using update to add item to dict
    print('\n', phonebook)
    phonebook.update({'David': '555-4444', 'Chris': '555-1234'})
    print('\n', phonebook)

    phonebook2 = {'Jim': '123-4567'}
    phonebook.update(phonebook2)
    print('\n', phonebook)

#first()

def second():
    test_scores = {
        'Kayla': [88, 92, 100],
        'Luis': [95, 74, 81],
        'Sophie': [72, 88, 91], 
        'Ethan': [70, 75, 78]}

    print(test_scores, '\n')

    # accessing values of different types
    kayla_scores = test_scores['Kayla']
    print(kayla_scores, '\n')
    print(kayla_scores[1], '\n')

    # initalize an empty dict
    empty ={}
    print(empty)
    empty[1] = 'this is a value'
    print(empty)

    # iterate over a dict
    phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
    for key in phonebook:
        print(key)

    for key in phonebook:
        print(key, phonebook[key])

    # the clear method
    # dictionary.clear()

    phonebook.clear()
    print(phonebook)

    # the get method
    # dictionary.get(key, default)    ** default = error message if nothing found

    phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}
    value = phonebook.get('Katie', 'Entry Not Found')
    print(value)

    value2 = phonebook.get('David', 'Entry Not Found')
    print(value2)

    # the items method
    # dictionary.items()

    print(phonebook.items())

    for key, value in phonebook.items():
        print(key, value)

    # they keys method
    # dictionary.keys()

    print(phonebook.keys())

    for key in phonebook.keys():
        print(key)

    # the values method

    print(phonebook.values())

    for value in phonebook.values():
        print(value)

    # the pop method
    # dictionary.pop(key, default)

    phone_num = phonebook.pop('Chris', 'Not Found')
    print(phone_num)
    print(phonebook)                                    # chris's value was returned to variable and whole pair was removed

    phone_num = phonebook.pop('Andy', 'Not Found')
    print(phone_num)
    print(phonebook)                                     # not found so nothing removed

    # the pop item

    key, value = phonebook.popitem()                        # pop item auto removes the last item (it takes no arguments)
    print(key, value)
    print(phonebook)

    phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}

#second()
# google iteritems....!!!!!
# google iteritems....!!!!

def multiDimDict():
    # Dict -> Dict
    my_dict = {'key1':{'nestedkey1':{'subnestedkey1':'subnestedValue'}}}
    print(my_dict)
    # output => {'key1':{'nestedkey1':{'subnestedkey1':'subnestedValue'}}}

    # Grab key 1's value
    print(my_dict['key1'])
    # output => {'nestedkey1': {'subnestedkey1': 'subnestedValue'}}

    # Grab nested key 1's value
    print(my_dict['key1']['nestedkey1'])
    # output => {'subnestedkey1': 'subnestedValue'}

    # Grab subnested key 1's value
    print(my_dict['key1']['nestedkey1']['subnestedkey1'])
    # output => subnestedValue

    # intialize instrument dict
    instruments ={'drums':{'color': 'black', 'sound': 'boom'}, 
                  'guitar':{'color': 'blue', 'sound': 'wahhh'}
    }
    print('original: ', instruments)

    # add something to nested
    instruments.update({'violin':{'color': 'brown', 'sound': 'whineeee'}})
    print('After updating: ', instruments)

    # more ways to add
    instruments['bass']= {'color': 'purple', 'sound': 'slapdabass'}
    print('After adding bass: ', instruments)

    # access items/nested items w/i out dict
    print('guitar: ', instruments['guitar'])
    print('guitar sound: ', instruments['guitar']['sound'])

    # iterate through nested dict
    for instruments, properties in instruments.items():
        print('Instrument: ', instruments)
        for prop in properties:
            print('\t', prop + ':', properties[prop])


multiDimDict()


# Sets

# sets contain a collection of unique values and works like a mathmatical set

# all the elements must be unique (aka use it to remove duplicates)

# sets are unordered, which mean that the elelemts are stored in no particular order

# the eleemnts that are stored ina  set can be of different data types
    
def firstSet():

    # creating a set
    my_set = set(['a', 'b', 'c'])                   # can be in any order
    print(my_set)

    my_set2 = set('abc')
    print(my_set2)                                  # separates out into each char

    my_set3 = set('aabbcc')
    print(my_set3)                                  # removes duplicate answers

    my_set4 = set('one two three')                  #set can only take one argument
    print(my_set4)

    my_set5 = {'one', 'two', 'three'}
    print(my_set5)

    # find length of my set
    lenght_set = len(my_set4)
    print(lenght_set)

    # adding and removing elements
    new_set = set()
    new_set.add(1)
    new_set.add(2)
    new_set.add(3)
    print('new set', new_set)

    new_set.update([4, 5, 6])
    print('after update', new_set)

    new_update = ([7, 8, 9])
    new_set.update(new_update)
    print('after var update', new_set)

    # removeing things
    new_set.remove(1)
    print('after value remove', new_set)

    #new_set.remove(10)                                             #error (keyError)
    #print('after value remove', new_set)

    #using discard
    new_set.discard(10)                                             #can handle errors
    print('after discard', new_set)

#firstSet()

def secondSet():

    #using loop to iterate thru a set
    new_set3 = set(['a', 'b', 'c'])
    for val in new_set3:
        print(val, end=' ')

    # using in and not in to test value
    numbers_set = ([1, 2, 3])
    if 1 in numbers_set:
        print('\nvalue in set')
    
    if 99 not in numbers_set:
        print('value is not in set')

    # find the union of sets
    set1 = set([1, 2, 3, 4])
    set2 = set([3, 4, 5, 6])
    set3 = set1.union(set2)
    print('set 1', set1)
    print('set 2', set2)
    print('set 3', set3)

    # you can also with unions
    set5 = set1 | set2                          #union is same as OR (or |)
    print('set 5', set5)
    

    # find the intersection
    set4 = set1.intersection(set2)
    print('set 4', set4)

    # youo can also with intersections
    set6 = set1 & set2                          #intersection same as AND (or &)
    print('set 6', set6)

    # with char
    char_set = set('abc')
    char_set2 = set('ABC')

    union_set = char_set | char_set2            #everything
    print('union char set', union_set)

    intersection_set = char_set & char_set2     #empty since there aren't the same
    print('inter char set', intersection_set)

    # find the difference in sets
    set7 = set1.difference(set2)                #whats in set 1 that's not in set 2
    set8 = set2.difference(set1)                #whats in set 2 that's not in set 1
    print('set 7', set7)
    print('set 8', set8)

    # another symbol
    set9 = set1 - set2
    print('set 9', set9)                        #same as set7

    # finding sysmetric difference of sets
    set10 = set1.symmetric_difference(set2)
    print('set 10', set10)

    # another symbol
    set11 = set1 ^ set2
    print('set 11', set11)

    # finding subsets and supersets
    set12 = set([1, 2, 3, 4])
    set13 = set([1, 2])
    print('subset', set13.issubset(set12))          #set 13 is a subset of set12    True
    print('subset', set12.issubset(set13))          #set 12 is a subset of set13    False
    print('superset', set12.issuperset(set13))          #set 13 is a subset of set12    True
    print('superset', set13.issuperset(set12))          #set 12 is a subset of set13    False

#secondSet()