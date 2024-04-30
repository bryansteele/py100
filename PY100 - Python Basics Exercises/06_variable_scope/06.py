a = 1

def my_function():
    a = 2

my_function()
print(a)

"""
Prints 1, because the variable `a` initialized at the top level has the value 1.
Inside a new variable `a` is initialized and assigned the value 2. This local
variable has no effect on the global variable `a`.
When we call print() after invoking the function, it refers to the gloabal variable.
"""