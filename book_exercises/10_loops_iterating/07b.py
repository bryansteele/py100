def find_integers(tup):
    nums = []
    for i in tup:
        if type(i) is int:
            nums.append(i)
    return nums



my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)

print(integers)


# OR

"""
def find_integers(tup):
    return [i
            for i in tup
            if type(i) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)

print(integers)
"""