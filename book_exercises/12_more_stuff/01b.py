def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# CHRIS

"""
The do_something function uses function composition and chaining to perform
several operations:
1. We first call dictionary.keys to get a dictionary view of all the keys for
the dictionary object.
2. We then use composition to call sorted on the dictionary view to get a
sorted list of the keys in the dictionary object.
3. Finally, we call the upper method on the key at index position 1.
"""