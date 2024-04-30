b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

"""
Prints [10, 2, 3], because `b[0] = 10` mutates the global variable `b`
"""
