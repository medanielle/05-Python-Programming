'''
                            Sequence Objects: Strings
>>> x = 'python is fun'
>>> x
'python is fun'
>>> 'don't'
  File "<stdin>", line 1
    'don't'
         ^
SyntaxError: invalid syntax
>>> "don't" 
"don't"
>>> 'don\'t' 
"don't"
>>> "\"yes\", they will" 
'"yes", they will'
>>> s = "FirstLine/nSecondLIne"
>>> s
'FirstLine/nSecondLIne'
>>> print(s)
FirstLine/nSecondLIne
>>> s = "FirstLine\nSecondLIne" 
>>> print(s)            
FirstLine 
SecondLIne
>>> s = r"FirstLine\nSecondLIne" 
>>> print(s)                     
FirstLine\nSecondLIne
>>>   
>>> print('C:\some\name')
C:\some
ame
>>> print("C:\some\name")
C:\some
ame
>>> print(r"C:\some\name")
C:\some\name
>>> print('C:\some\\name')
C:\some\name

>>> text = ('This is a run on sentence'
... 'it con go on forever')
>>> text
'This is a run on sentenceit con go on forever'
>>> prefix = 'py'
>>> suffix = 'thon'
>>> word = prefix + suffix 
>>> word
'python'

>>> word[1]
'y'
>>> word[-1] 
'n'
>>> word[0:2]
'py'
>>> word[0:5:2] 
'pto'
>>> word[0:5:-1] 
''
>>> word[2:5]   
'tho'
>>> word[:2] 
'py'
>>> word[::2] 
'pto'
>>> word[::-1] 
'nohtyp'
>>> word[2:]   
'thon'
>>> word[-2]  
'o'
>>> word[-2:] 
'on'
>>> word[-2::-1] 
'ohtyp'
>>> len(word)
6
>>> sorted(word)
['h', 'n', 'o', 'p', 't', 'y']
>>> upper(word)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'upper' is not defined
>>> word.upper
<built-in method upper of str object at 0x0000020FDE1480F0>
>>> word.upper()
'PYTHON'
>>> word.lower()  
'python'
>>> word.title() 
'Python'

>>> x = "I am a string"
>>> x
'I am a string'
>>> ord(x[0])
73
>>> x[0]
'I'
>>> hex(ord(x[0]))
'0x49'
>>> hex(73)       
'0x49'
>>> x = b"I am a string" 
>>> type(x)             
<class 'bytes'>
>>> x = u"I am a string" 
>>> type(x)
<class 'str'>

>>> word = 'python'
>>> z in word
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> o in word
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'o' is not defined
>>> 'o' in word 
True
>>> 'z' not in word
True

>>> name = input("What is your name? ")
What is your name? Danielle
>>> name
'Danielle'
>>> my_string = "Hello World!"
>>> a = my_string.upper()
>>> print(a)
HELLO WORLD!
>>> a = len(my_string)
>>> a
12
>>> a = my_string.split(" ")
>>> a
['Hello', 'World!']
>>> print(my_string)
Hello World!
>>> b = "+".join(a)
>>> print(b)
Hello+World!
>>> b = " ".join(a)
>>> print(b)
Hello World!
>>> my_string[1]
'e'
>>> my_string[1] = "E"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> x = 'blue,red,green'
>>> x.split(',')
['blue', 'red', 'green']
>>> x[1]
'l' 
>>> x
'blue,red,green'
>>> y = x.split(',') 
>>> y
['blue', 'red', 'green']
>>> y[1]
'red'
>>> a,b,c = x.split(',') 
>>> a
'blue'
>>> b 
'red'
>>> c
'green'
>>> s = '-'
>>> seq = ("a", "b", "c")
>>> print(s.join(seq))
a-b-c
>>> new_seq = s.join(seq) 
>>> new_seq
'a-b-c'
>>> seq
('a', 'b', 'c')

'''

"""
>>> def split(word):  
...     return [char for char in word]  
... 
>>> word = 'geeks'
>>> print(split(word))
['g', 'e', 'e', 'k', 's']
