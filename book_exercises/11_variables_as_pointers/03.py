dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

"""
The constructor call dict(dict1) creates a new dict that contains the same key/
value pairs as dict1.
When we change the value with the 'Montey Python' key in dict2, we don't see a
change in dict 1.
The two objects are identical, but NOT the same object.
"""