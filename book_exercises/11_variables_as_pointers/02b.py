set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

"""
{42, 'Monty Python', range(5, 10), ('a', 'b', 'c')}

set1 and set2 both reference the same set.
When adding another element to the set1, we see the changes in set2 also.
This also demonstrates that assigning a variable to another variable doesn't
create a new object, but it copies a reference from the original variable into
the target variable.
"""