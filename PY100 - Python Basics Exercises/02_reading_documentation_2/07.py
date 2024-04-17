"""
The keyword in
https://docs.python.org/3/reference/expressions.html#in


The str.find() method, almost does what we want - it returns the index of the
matching substring, but raises an error if there is no match. However, in the
description for the find method, you'll learn that you can use in to determine
whether a substring is found in a string; this note links to the description of
in in the Membership test operations section.
The find() method should be used only if you need to know the position of sub.
To check if sub is a substring or not, use the in operator:

https://docs.python.org/3/library/stdtypes.html#str.find

str.find(sub[, start[, end]])
"""

string = "Hello, World!"
print("World in string")
print("Python" in string)