def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

"""
Outputs Empty, becase an empty list is falsy, the else block runs instead of
the if block
"""