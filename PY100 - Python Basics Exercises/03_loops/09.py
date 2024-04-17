fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == "Nemo":
        break

print()

# Further Exploration w/ while loop

x = 0
while x < len(fish_list):
    print(fish_list[x])
    if fish_list[x] == 'Nemo':
        break

    x += 1

