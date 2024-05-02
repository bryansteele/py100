scores = [96, 47, 113, 89, 100, 102]
n = 0

for x in scores:
    if x >= 100:
        n += 1

print(n)


# OR
print()

a = [i for i in scores if i >= 100]
print(len(a))