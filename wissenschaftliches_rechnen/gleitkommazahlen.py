import numpy as np

numbers = [14, 2.3792, 3 + 7j, np.int32(-11), np.uint32(5), np.float64(8.23)]

for num in numbers:
    print("{:10}:\t{}".format(num, type(num)))

print("------------------------------------------")

ergebnis = np.sqrt(2)
print(ergebnis * ergebnis == 2)
print(np.isclose(ergebnis * ergebnis, 2))

print(ergebnis)
print(ergebnis * ergebnis)

print("------------------------------------------")

ergebnis = np.sin(np.pi)
print(ergebnis)
print(ergebnis == 0)
print(np.isclose(ergebnis, 0))

print("------------------------------------------")

print(np.finfo(np.float32).min)
print(np.finfo(np.float32).max)
print(np.finfo(np.float64).min)
print(np.finfo(np.float64).max)

print(np.finfo(np.float32).tiny)
print(np.finfo(np.float64).tiny)

print("------------------------------------------")

a = 2 ** 24
b = np.float32(a + 1)

print(a)
print(b)
