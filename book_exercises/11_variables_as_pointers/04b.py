dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

"""
[1, 42, 3]

The dict constructor creates a shallow copy. Mutations to the dict1['a']
can be seen in dict2['a'].
"""