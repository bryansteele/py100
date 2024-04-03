my_list = [6, 3, 0, 11, 20, 4, 17]

x = 0
while x < len(my_list):
    if my_list[x] % 2 == 0:
        print(my_list[x])
    x += 1

print()

for num in my_list:
    if num % 2 != 0:
        print(num)