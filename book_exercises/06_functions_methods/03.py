def multiply(num1, num2):
    return float(num1) * float(num2)

number1 = input('Enter the fist number: ')
number2 = input('Enter the second number: ')
total = multiply(number1, number2)
print(f'{number1} * {number2} = {total}')