import numpy as np

"""
# LGS - Lösung mit Gauß
A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
])

b = np.array([0, 5, 3])


print("Lösung mit Gauß:")
print(np.linalg.solve(A, b).round().astype(int)) # [-1 -4  3]

"""

A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
], dtype='float')

b = np.array([0, 5, 3])

Ab = np.hstack([A, b.reshape(-1, 1)])

n = len(b)

for i in range(n):
    a = Ab[i]

    for j in range(i + 1, n):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

for i in range(n - 1, -1, -1):
    Ab[i] = Ab[i] / Ab[i, i]
    a = Ab[i]

    for j in range(i - 1, -1, -1):
        b = Ab[j]
        m = a[i] / b[i]
        Ab[j] = a - m * b

x = Ab[:, 3]
