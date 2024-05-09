numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

"""
The range() function by default, starts with 0, not 1. So to fix the issue above,
I added 0 to the `start` posistion and changed the 5 to a 6, in the `end`
position, because it goes UP TO the stated number, but does NOT include the
stated number.
"""

