"""
counter = 0

while counter < 5:
    print(counter)

There is nothing incrementing the counter variable, which has a value of 0.
The loop conditional will keep running because counter will always be less
than 5. counter < 5 will always return a truthy value.
"""

counter = 0

while counter < 5:
    print(counter)
    counter += 1

