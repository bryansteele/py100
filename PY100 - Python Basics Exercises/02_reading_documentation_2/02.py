# https://peps.python.org/pep-0008/

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

"""
The following were not followed in the original code snippet:

1. Variable Naming: Variables should be in snake_case instead of camelCase.
2. Spacing: There shouldn't be a space before the colon in the while loop.
3. Missing Spaces: There should be a single space on both sides of the =, >,
and -= operators.
"""