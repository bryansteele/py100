def even_or_odd(num):
    return int(num) % 2 == 0

number = input('Enter an integer: ')

if even_or_odd(number):
    print('even')
else:
    print('odd')



'''
def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

OR

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')
'''