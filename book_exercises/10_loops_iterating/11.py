my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

i = 0
while i < len(my_list):
    j = 0
    while j < len(my_list[i]):
        number = my_list[i][j]
        if number % 2 ==0:
            print(number)

        j += 1

    i += 1
