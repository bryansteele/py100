cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city != None:
        print(len(city))
    else:
        continue

print()

for city in cities:
    if city is None:
        continue

    print(len(city))