list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

"""
Prints `True`.
When comparing two lists using ==, the comparison is based on the values
contained within the list, not their identity(memory location). If the lists
contain the same values in the same order, it will return `True`.

However the `is` operator will return `False`
"""