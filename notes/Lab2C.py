""">>> def getTax(subtotal, tax)
  File "<stdin>", line 1
    def getTax(subtotal, tax)
                            ^
SyntaxError: invalid syntax
>>> def getTax(subtotal, tax):
...     total = (subtotal * tax) + subtotal
... return total
  File "<stdin>", line 3
    return total
    ^
SyntaxError: invalid syntax
>>> def getTax(subtotal, tax):          tal
...     return (subtotal * tax) + subtotal
...
>>> getTax(1,2)                        tal
3
>>> getTax(10, .01)
10.1
>>> getTax(10, .1)
11.0
>>> 
"""

subtotal = float(input("Enter subtotal: "))
tax = .1
total = (subtotal * tax) + subtotal
round(total, 2)
print("Here is the Total with tax", total)
