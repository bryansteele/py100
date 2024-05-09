def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

"""
The return value of a function is determined by the explicit `return` statement.
If no return statement, the function will implicitly return `None`.

To fix this problem, we add a `return` statement to all three `if` statements.
"""