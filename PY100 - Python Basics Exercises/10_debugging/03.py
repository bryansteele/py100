def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

"""
input() returns a string. and the funtion that it is passed to is concatenating
intstead of multiplying an integer.

I fix this by converting the string to an int prior to passing it to the function
"""