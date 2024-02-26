foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)


# Prints bar to the screen. The foo variable on line 4 is created inside the
# function and shaddows the foo variable on line 1, so line 4 does not change
# the value from line 1.