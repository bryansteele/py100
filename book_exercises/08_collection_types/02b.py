stuff = ('hello', 'world', 'bye', 'now')
list_stuff = list(stuff)
list_stuff[2] = 'goodbye'
stuff = tuple(list_stuff)
print(stuff)

# OR

stuff = ('hello', 'world', 'goodbye', 'now')

# OR

stuff = stuff[0:2] + ('goodbye', stuff[3])


"""
Since tuples are immutable, you can't replace the element 'bye'. You can only
creat a new tuple and reassign it.
"""
