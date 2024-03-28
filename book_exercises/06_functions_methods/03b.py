def multiply(num1, num2):
    return float(num1) * float(num2)

first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')

product = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')