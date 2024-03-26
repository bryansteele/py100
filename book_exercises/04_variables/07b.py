NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

"""
It first greets Victor 3x and then it greets Nina 3x.
Although NAME is a constant. Python does not support real constants.
There is NO way in Python to keep them from being changed. If this faux-constant
needs to be chaged, then a regular variable should be used instead.
"""