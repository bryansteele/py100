dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

"""
The Life of Brian

The constructor call dcit(dict1) creates a new dict that contains the same
key/value pairs as dict1. They are not the same object, so when changing the
value associated with the 'Monty Python' key in dict2, we don't see the change
in the dict1.

This demonstrates that two identical objects aren't necessarily the same object.
"""
