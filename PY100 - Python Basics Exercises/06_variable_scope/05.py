a = 1

def my_function():
    print(a)
    a = 2

my_function()

"""
Raises an UnboundLocalError: local variable 'a' referenced before assignment

Python detects that `a` is being assigned within the function and therefore
treats it as a local variable.
However, since we are trying to print the local `a` variable's value before it
has been assigned a value, we get an error.
"""