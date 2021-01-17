import functools

def anwenden(f, liste):
    ergebnis = []
    for element in liste:
        ergebnis.append(f(element))
    print(ergebnis)


anwenden(lambda x: x + 42, range(10))

for i in [17, 22, 42]:
    anwenden(lambda x: x + i, range(10))


print(list(map(lambda x: x + 42, range(10))))

# ---------------------------------------------

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# -----------------------------------------

ergebnis = functools.reduce(lambda x, y: x+y, [47, 11, 42, 13])
print(ergebnis)
