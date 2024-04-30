def is_empty(x):
    return  x == ""  # OR    return len(x) == 0


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


# OR
print()


def is_empty(y):
    return not y

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True