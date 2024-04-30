x = 10

def my_function():
    x = x + 5
    print(x)

my_function()


"""
Raises an UnboundLocalError: local variable 'x' referenced before assignment

In the function, when we attempt to reassign the value of x by incrementing it,
Python assumes it is a local variable, since we are assigning it inside the
function. However, it is uninitialized and we get an error.
"""