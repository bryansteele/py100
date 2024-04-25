def compare_by_length(x, y):
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        return 0

print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0