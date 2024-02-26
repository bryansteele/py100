def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


'''
Line 1 - multiply, left, right
Line 2 - left, right
Line 4 - get_num, prompt
Line 5 - float, input, prompt
Line 7 - first_number, get_num
Line 8 - second_number, get_num
Line 9 - product, multiply, first_number, second_number
Line 10- print, first_number, second_number, product
'''