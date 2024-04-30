def my_function():
    a = 1

    if True:
        print(a)

my_function()

"""
Outputs 1 to the terminal, because variables initialized inside the same scope
where a block begins can be accessed inside the block.
Variable a is initialized within the function and then accessed inside the if
statement block.
"""