def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])


# Prints Empty, because an empty list evaluates to a falsy value. So, the else 
# block is run and prrints out Empty