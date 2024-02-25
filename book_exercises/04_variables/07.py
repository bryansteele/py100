NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)


"""
It will output the follow, because Python does not make sure constants are not
reassigned. There are no real constants in Python. The programmer has to make
sure that is true.

Good Morning, Victor
Good Afternoon, Victor
Good Evening, Victor
Good Morning, Nina
Good Afternoon, Nina
Good Evening, Nina
"""