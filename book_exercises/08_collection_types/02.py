stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

print(stuff)



# Tuples are not mutable. So, at best we can create a new tuple and reassign
# 'bye' with 'goodbye'
