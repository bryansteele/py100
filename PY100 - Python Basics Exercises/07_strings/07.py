def is_empty_or_blank(x):
    return x.strip(' ') == ''

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


# OR
print()


def is_empty_or_blank(y):
    return len(y.strip(' ')) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True



# OR
print()


def is_empty_or_blank(z):
    return not z.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True