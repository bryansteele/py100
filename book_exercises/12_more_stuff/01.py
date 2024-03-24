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

"""
CHRIS

1st, we call `dictionary.keys` to get a dictionary view of all the keys for the
`dictionary` object.

2nd, we use composition to call `sorted` on the dictionary view to get a sorted
list of the keys for the `dictionary` object.

3rd, we use chaining to get the sorted `dictionary` key at index position 1.

4th, we call the `upper` method on the key at index position 1.

"""
