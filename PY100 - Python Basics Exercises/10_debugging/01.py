def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

"""
TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given

The function is set to accept 1 argument(a list of integers) and the invocation
is trying to pass in 6 arguments.

If you comment out the 1st invocation you will also see this exception raised:
TypeError: 'int' object is not iterable

Meaning, although it is one argument, it is an integer and you can not iterate
over an integer object
"""