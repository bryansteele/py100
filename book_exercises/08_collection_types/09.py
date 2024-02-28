my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

#1 Yes, they are equal. Both lists with the same elements.
print(my_list == another_list)

#2 No, they are not the same object. The list constructor creates a new object.
print(my_list is another_list)

#3 The nested list at index 3 are equal. They both have the same elements.
print(my_list[3] == another_list[3])

# 4 The nested lists at index 3 are the same object. The list constructor creates
# a shallow copy of the iterable passed as an argument. Shallow copies don't
# create new nested lists. Instead, only a reference to the nested list gets copied.
print(my_list[3] is another_list[3])