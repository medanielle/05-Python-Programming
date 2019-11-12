import datetime

today = datetime.datetime.now()
print(str(today))
    # output =>    2019-11-12 12:46:19.155530
print(repr(today))
    # output = >    datetime.datetime(2019, 11, 12, 12, 46, 19, 155530)


import keyword

print(keyword.kwlist)
    # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(keyword.iskeyword('break'))
    # True