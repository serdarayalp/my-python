import numpy as np

# Operatoren und Skalare

lst = [2, 3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9]
v = np.array(lst)

print(v + 2)
print(v - 1.38)
print(v * 2.2)
print(v ** 2)
print(v ** 1.5)

# Arithmetische Operationen auf zwei Arrays

A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
B = np.array([[5, 4, 2], [1, 0, 2], [3, 8, 2]])

print("Addition zweier Arrays: ")
print(A + B)

print("\nMultiplikation zweier Arrays: ")
print(A * B)

print("-------------------------------------------------------")

# Matrizenmultiplikation und Skalarprodukt

"""
numpy.dot(a, b, out=None)
    If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
    If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.
    If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.
    If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
    If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:
        dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
"""

A = np.array([1, 2, 3])
B = np.array([1, 2, 3])
print(np.dot(A, B))


A = np.array([[1, 2], [1, 2]])
B = np.array([[1, 2], [1, 2]])
print(np.dot(A, B))
print(A@B)

print("-------------------------------------------------------")

A = np.array([[1, 2], [1, 2]])
print(A * 2)
print(np.multiply(A, 2))
print(np.dot(A, 2))

print("-------------------------------------------------------")

A = np.array([[1, 2], [1, 2]])
print(A.shape)
B = np.array([1, 2])
print(B.shape)
C = np.array([[1], [2]])
print(C.shape)

print("\n MATRIX.dot(VECTOR)")
ergebnis = np.dot(A, B)
print(ergebnis)
print(ergebnis.shape)

print("\n MATRIX.dot(VECTOR_MATRIX)")
ergebnis = np.dot(A, C)
print(ergebnis)
print(ergebnis.shape)

print("-------------------------------------------------------")

A = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])  # 3x3
B = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])  # 3x4
print(np.dot(A, B))

print("-------------------------------------------------------")

print(np.dot(3, 4))

x = np.array([3])
y = np.array([4])
print(np.dot(x, y))

x = np.array([3, -2])
y = np.array([-4, 1])

print(np.dot(x, y))

print("-------------------------------------------------------")

A = np.array([[11, 12, 13, 14],
              [21, 22, 23, 24],
              [31, 32, 33, 34]])
B = np.array([[5, 4, 2],
              [1, 0, 2],
              [3, 8, 2],
              [24, 12, 57]])
print(np.dot(A, B))

"""
Damit die Matrizenmultiplikation (also dot) für zwei Matrizen A und B im zweidimensionalen 
Fall funktionieren kann, muss gelten:

A.shape[-1] == B.shape[0]
"""

# es muss gelten:
print(A.shape)
print(A.shape[-1])
print(B.shape)
print(B.shape[0])
print(A.shape[-1] == B.shape[0])


print("-------------------------------------------------------")

# Das dot-Produkt im 3-dimensionalen Fall

"""
numpy.dot(a, b, out=None)
    If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:
        dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
"""

# Vergleichsoperatoren
A = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
B = np.array([[11, 102, 13], [201, 22, 203], [31, 32, 303]])
print(A == B)

print(np.array_equal(A, B))
print(np.array_equal(A, A))


# Logische Operatoren

a = np.array([[True, True], [False, False]])
b = np.array([[True, False], [True, False]])
print(np.logical_or(a, b))
print(np.logical_and(a, b))
