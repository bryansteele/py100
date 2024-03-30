def upcase(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str

print(upcase('hello world'))
print(upcase('goodbye'))