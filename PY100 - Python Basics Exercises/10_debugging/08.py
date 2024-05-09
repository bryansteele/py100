
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix)

"""
Without list.copy(), any modification made to one sub-list impacts all the
sub-lists. They essentially reference the same object.

With list.copy(), it generates a shallow copy of the list object and the three
nested sub-lists will individually reference distinct objects.
"""