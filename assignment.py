a = ['a', 'c', 'e', 3, 5, 7, True, False]

b = ['a', 'd', 'f', 4, 8, 9, True, False]

print(a[1])

for x in range(len(b)):
    print(b[x])

minseon = {
    "name": "sunny",
    "year": 1996,
    "health": 80,
    "power": 90,
    "armor": "level 3 vest",
    "hat": "level 3 helmet",
    "bag": "level 3 bag pack",
}

for x, y in minseon.items():
    print(x, y)
