destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(element, lst):
    for item in lst:
        if item == element:
            return True
    return False


print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))

# OR
print()


def contains(element, lst):
    i = 0
    while i < len(lst):
        if lst[i] == element:
            return True
        i += 1
    return False

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
