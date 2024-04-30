a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

"""
Prints 2, because we are using the `global` statement which tells Python to
use the variable in the global scope. Which means anything done to the variable
inside the function will also affect the global variable.
Inside the function we reassign the variable `a` to the value 2, which has also
changed the global variable to 2.
"""