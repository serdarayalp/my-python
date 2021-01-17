import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.prod(A.shape))

# print(np.prod((1, 2, 3, 4)))
# print(np.prod(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

B = A.reshape((6,))

print(B)

print("-------------------------------------------------------")

X = np.array(range(24))
print(X)

Y1 = X.reshape((3, 4, 2))
print(Y1)

Y2 = Y1.reshape((2, 3, 4))
print(Y2)

print("-------------------------------------------------------")

x = np.array([11, 22])
y = np.array([18, 7, 6])
z = np.array([1, 3, 5])

c = np.concatenate((x, y, z))
print(c)

print("-------------------------------------------------------")

"""
Wenn wir multidimensionale Arrays zusammenführen, müssen wir auf die Achsen achten. Die Arrays 
müssen die gleiche Shape haben, um mit concatenate zusammen gefügt werden zu können. Bei multidimensionalen 
Arrays können wir diese entsprechend anordnen. Der Default-Wert ist axis = 0:
"""

x = np.array(range(12))
x = x.reshape((3, 4))

y = np.array(range(100, 112))
y = y.reshape((3, 4))

z = np.concatenate((x, y))

print(z)
print(z.shape)


z = np.concatenate((x, y), axis=1)
print(z)
print(z.shape)

print("-------------------------------------------------------")

# Weitere Dimensionen hinzufügen

x = np.array([2, 5, 18, 14, 4])
print(x)

y = x[:, np.newaxis]
print(y)

print("-------------------------------------------------------")

# "Fliesen" mit "tile"
x = np.array([ [1, 2], [3, 4]])
print(np.tile(x, (3, 4)))

