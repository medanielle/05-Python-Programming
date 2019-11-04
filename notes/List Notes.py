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

first()
