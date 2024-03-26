obj = 42

obj = 'ABcd'        # reassigns
obj.upper()         # neither
obj = obj.lower()   # reassigns
print(len(obj))     # neither
obj = list(obj)     # reassigns
obj.pop()           # mutates
obj[2] = 'X'        # mutates
obj.sort()          # mutates
set(obj)            # neither
obj = tuple(obj)    # reassigns