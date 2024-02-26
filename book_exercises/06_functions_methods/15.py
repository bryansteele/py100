def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


'''
Line 1 - multiply (Global) // left, right (Local)
Line 2 - left, right (Local)
Line 4 - get_num (Global) // prompt (Local) 
Line 5 - float, input (Built-in) // prompt (Local)
Line 7 - first_number, get_num (Global)
Line 8 - second_number, get_num (Global)
Line 9 - product, multiply, first_number, second_number (Global)
Line 10- print (Built-in) // first_number, second_number, product (Global) 
'''