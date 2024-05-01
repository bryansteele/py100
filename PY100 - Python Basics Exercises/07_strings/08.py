a = 'launch school tech & talk'
b = a.title()
print(b)


# OR


def cap_words(string):
    words = string.split(' ')
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())

    return ' '.join(capitalized_words)

string = 'launch school tech & talk'
result = cap_words(string)
print(result)