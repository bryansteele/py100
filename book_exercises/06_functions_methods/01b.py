def set_foo():
    foo = 'bar'

set_foo()
print(foo)

"""
Try to print foo to the terminal but becasue foo is initialized inside the
function block, print() can not access it. So, a NameError is raised.
"""