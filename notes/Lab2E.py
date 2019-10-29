my_str = input("Please enter a string: \n")
#print("number of characters in string:\n", len(my_str))
print("number of characters in string:\n" + str(len(my_str)))
print("number of words in string:\n" + str(len(my_str.split())))
upper_count = 0
lower_count = 0
other_char = 0

for char in my_str:
    if char.isupper() == True:
        upper_count += 1
    elif char.islower() == True:
        lower_count += 1
    else:
        other_char += 1

print("# of upper case:\n" + str(upper_count))
print("# of lower case:\n" + str(lower_count))


"""
print ("upper:", len(re.findall("[A-Z]", user_input)))