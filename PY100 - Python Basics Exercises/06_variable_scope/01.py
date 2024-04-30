if True:
    my_value = 20

print(my_value)

"""
Prints out 20.
Variables initialized inside a block are accessible outside that block. 
"""


print()



if False:
    my_new_value = 42

print(my_new_value)

"""
Raises a NameError: name 'my_new_value' is not defined

Since the if statement will always be False, the variable is never initialized.
"""