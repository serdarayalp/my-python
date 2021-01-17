from math import sqrt

# Listen-Abstraktion (List Comprehension)
squares = [n*n for n in range(10)]
print(squares)

# Generatoren-Abstraktion (generator comprehension)
x = (x ** 2 for x in range(20))
print(x)
print(list(x))

# Mengen-Abstraktion
x = {x ** 2 for x in range(20)}
print(x)

