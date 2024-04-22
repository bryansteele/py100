def cite(str1, str2):
    print(f'{str1} said: "{str2}".')

cite('Bruce Eckel', 'Python is executable pseudocode.')

print()

# OR with the format method:

def cite(author, quote):
    print('{} said: "{}"'.format(author, quote))