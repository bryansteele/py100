foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

"""
The program prints `bar`. The assignment on line 4 creates a new variable that's 
local to the function.
"""