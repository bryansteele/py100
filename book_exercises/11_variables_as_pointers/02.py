set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)


# {('a', 'b', 'c'), 42, range(5, 10), 'Monty Python'}
# set1 and set2 reference the same set. They are two aliases for the same set.
# So, adding to set2 or set1 will be reflected by the other.