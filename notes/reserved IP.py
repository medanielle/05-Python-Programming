import sys

#checking octets
def ip_addr_valid(list):
    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split('.')

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254):
            continue

        else:
            print("\n There was an invalid IP address in the file: {} :( \n".format(ip))
            sys.exit()


"""
a = open(r"D:\PySamples\IPAddressDemo\ip.txt")          *** or \\ to escape each backslash
a.readlines()
['10.10.10.2\n', '10.10.10.3\n', ...]
THEN RESET!! 
a.seek(0)
for i in a.readlines():                                 *** removes the \n for the right (aka r strip)
    i.rstrip("\n")
'10.10.10.2'
'10.10.10.3'
...
a.seek(0)
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string_input = (input("Enter a string to Encrypt: ")).upper()
input_length = len(string_input)
encrypted_string = ''
shiftNum = int(input('Enter a value to shift by: '))

for i in range(input_length):
    location = alpha.find(string_input[i])
    new_location = (location + shiftNum) % 26
    # if new_location >= 26:   replace with   %26   one line up
    #     new_location -= 26
    encrypted_string += alpha[(new_location)]
print('Encrypted text:', encrypted_string)
