"""
Nothing seen in the List documents as to what happens when trying to access an
out of bounds index, but it does raises an exception, IndexError: list index
out of range.
Docs for the exception can be found here:
https://docs.python.org/3/library/exceptions.html#IndexError
"""

print(['fish', 'and', 'chips'][6])