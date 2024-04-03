age = input('What is your age? ')

print(f'You are {age} years old.')

print()

for x in range(10, 40, 10):
    print(f'In {x} years, you will be {int(age) + x} years old.')