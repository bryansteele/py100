def number_range(int):
    if int < 0:
        print(f'{int} is less than 0')
    elif int < 51:
        print(f'{int} is between 0 and 50')
    elif int < 101:
        print(f'{int} is between 51 and 100')
    else:
        print(f'{int} is greater than 100')

number_range(0)
number_range(25)
number_range(50)
number_range(75)
number_range(100)
number_range(101)
number_range(-1)