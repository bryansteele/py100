my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal
# YES, they are both lists with the same element
print(my_list == another_list)

# Are the lists assigned to my_list and another_list the same object?
# NO, the list constructor creates a new list
print(my_list is another_list)

# Are the nested lists at index 3 of my_list and another_list equal?
# YES, they are both lists that have the same elements
print(my_list[3] == another_list[3])

# Are the nested lists at index 3 of my_list and another_list the same object?
# YES, the list constructor creats a shallow copy fo the iterable passed as an
# argument. Shallow copies don't create new lists. instead, only a reference to
# the nested list gets copied.
print(my_list[3] is another_list[3])
