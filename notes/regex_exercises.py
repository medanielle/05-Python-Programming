import re
"""
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
"""
def find_words():
    string = '''
    bat bit but hat hit hut 
    mut wut tit mat
    '''
    pattern = re.compile(r'[bh][aiu]t')
    listy = pattern.findall(string)

    print(listy)

    matches = pattern.finditer(string)
    for match in matches:
        print(match.group(0))

#find_words()

"""
2. Match any pair of words separated by a single space, that is,
first and last names.
"""
def find_names():
    string = '''
    First Last
    middle last
    djffdjjkdfjkd
    '''
    pattern = re.compile(r'\w+\s\w+')
    listy = pattern.findall(string)

    print(listy)

    matches = pattern.finditer(string)
    for match in matches:
        print(match.group(0))

# find_names()

"""
3. Match any word and single letter separated by a comma and
single space, as in last name, first initial.
"""

def find_initial():
    string = '''
    Last, F
    last, m
    djffdjjkdfjkd dsfdsgdfg
    '''
    pattern = re.compile(r'\w+,\s\w?', re.MULTILINE)
    listy = pattern.findall(string)

    print(listy)

    matches = pattern.finditer(string)
    for match in matches:
        print(match.group(0))

#find_initial()

"""
4. Match the set of all valid Python identifiers.

Rules for Python Identifiers
An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
​
Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. Names like myClass, var_1 and print_this_to_screen, all are valid example.
​
An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
​
Keywords cannot be used as identifiers. 
​
We cannot use special symbols like !, @, #, $, % etc. in our identifier.
​
Identifier can be of any length.
​
​
Keywords in Python:
​
(False) | (class) | (finally) | (is) | (return) | (None) | (continue) ) | (
"""



def find_identifiers():
    string = ''' False 1variablE @vARIABLE variable apple'''
    pattern = re.compile(r'(\s[a-zA-z]+) | (?!False)')
    # '(False) | (class) | (finally) | (is) | (return) | (None) | (continue) | (\d+) | '
    listy = pattern.findall(string)

    print(listy)

# find_identifiers()
"""
5. Match a street address according to your local format (keep
your regex general enough to match any number of street
words, including the type designation). For example, American
street addresses use the format: 1180 Bordeaux Drive. Make
your regex flexible enough to support multi-word street
names such as: 3120 De la Cruz Boulevard.
"""
def find_addr():
    string = """
    1234 Place Street
    1180 Bordeaux Drive
    3120 De la Cruz Boulevard
    """

    pattern = re.compile(r'(\d+)([a-zA-z ]+)(Street|Drive|Boulevard)')
    matches = pattern.findall(string)
    for match in matches:
        print(match)


# find_addr()

"""
6. Match simple Web domain names that begin with “www.”
and end with a “.com” suffix; for example, www.yahoo.com.
Extra Credit: If your regex also supports other high-level
domain names, such as .edu, .net, etc. (for example,
www.foothill.edu).
"""
urls = """
http://testsite.com
https://www.google.com
https://youtube.com
https://www.nasa.gov
www.website.com
"""

def find_urls_groups():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(urls)

    for match in matches:
        print(match.group(0, 1, 2, 3, 4))

# find_urls_groups()

"""
7. Match the set of all valid e-mail addresses (start with a loose
regex, and then try to tighten it as much as you can, yet
maintain correct functionality). Try to break what we did in class 
and improve it.
"""

email = """ 
TestUser@gmail.com
test.user@school.edu
test-123-user@this-place.net
bademail@.com
"""

def find_emails_mine():
    pattern = re.compile(r'([a-zA-Z.0-9-_+]+)(@[a-zA-Z.0-9-_]+)(\.[a-zA-Z.0-9-_]+)')
    matches = pattern.finditer(email)

    for match in matches:
        print(match.group(0))

find_emails_mine()

"""
8. Match the set of all valid Web site addresses (URLs) (start
with a loose regex, and then try to tighten it as much as you
can, yet maintain correct functionality).Try to break what we did in 
class and improve it.
"""


"""
9. type(). The type() built-in function returns a type object,
which is displayed as the following Pythonic-looking string:

    # >>> type(0)
    # <type 'int'>
    # >>> type(.34)
    # <type 'float'>
    # >>> type(dir)
<type 'builtin_function_or_method'>

Create a regex that would extract the actual type name from
the string. Your function should take a string like this <type
'int'> and return int. (Ditto for all other types, such as
‘float’, ‘builtin_function_or_method’, etc.) Note: You
are implementing the value that is stored in the __name__
attribute for classes and some built-in types.
"""
types - """
<class 'int'>
<class 'str'>
<class 'builtin_function_or_method'>
<class 'float'>
"""
def get_type():


"""
11. Processing Dates. In Section 1.2, we gave you the regex pattern
that matched the single or double-digit string representations of
the months January to September (0?[1-9]). Create the regex
that represents the remaining three months in the standard
calendar.
"""