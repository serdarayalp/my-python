import numpy as np
from scipy.linalg import solve_triangular


np.set_printoptions(suppress=True)


a = np.array([1, 2, 3])
print(a)  # [1 2 3]

b = np.zeros_like(a)
print(b)  # [0 0 0]

# ein Vektor mit drei zufälligen Zahlen
c = np.random.rand(3)
print(c)  # [0.13263865 0.73646975 0.49944332]

d1 = np.ones((4,))
print(d1)  # [1. 1. 1. 1.]
d2 = np.ones((4, 2))
print(d2)
"""
[[1. 1.]
 [1. 1.]
 [1. 1.]
 [1. 1.]]
"""
d3 = np.ones((4, 2, 3))
print(d3)
"""
[
 [[1. 1. 1.][1. 1. 1.]]
 [[1. 1. 1.][1. 1. 1.]]
 [[1. 1. 1.][1. 1. 1.]]
 [[1. 1. 1.][1. 1. 1.]]]
"""

e = np.ones(4)
print(e)  # [1. 1. 1. 1.]

f = np.ones((4, 1))
print(f, f.shape)
"""
[[1.]
 [1.]
 [1.]
 [1.]] (4, 1)
"""

h1 = np.array([1, 2, 3.0])
print(h1, h1.dtype)  # [1. 2. 3.] float64

h2 = np.array([1, 2, 3])
print(h2, h2.dtype)  # [1 2 3] int64

h3 = np.array([1, 2, 3], dtype=complex)
print(h3, h3.dtype)  # [1.+0.j 2.+0.j 3.+0.j] complex128

i = np.array([1, 2, 3])
print(a + a)
print(a * a)
print(a / a)
print(a - a)
print(a * 2)
print(-a)

print(i.argmax())
print(max(i))
print(i.sum())
print(abs(-i))

print(i[0])
print(i[0:2])
print(i[:-2])


def dot_p(a, b):
    assert a.shape == b.shape

    c = 0.0
    for i in range(a.size):
        c += a[i] * b[i]
    return c


a = np.array([1, 2, 3])
b = np.random.rand(3)

try:
    print(dot_p(a, b))
except ValueError as e:
    print(e)

v1 = np.array([1, 0])
v2 = np.array([0, 1])
v3 = np.array([2, 0])
v4 = np.array([1, 1])

print(v1.dot(v2))  # 0, beide Vektoren sind senkrecht zueinander
print(v1.dot(v3))  # 2
print(v1.dot(v4))  # 1

print(np.linalg.norm(v4))
print(v4 / np.linalg.norm(v4))  # Normalisieren des Vektors

# Explicit definition of a matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A)
print(A.shape)

x = np.array([1., 2., 3.])
print(x.shape)

y = A.dot(x)
print(y.shape)

# ---------------------------------

print(np.eye(3))

print(np.ones((3, 3)))
print(np.pi * np.ones((3, 3)))

# ---------------------------------

# Random matrix, accessing elements
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
R = np.random.rand(3, 3)
print(B)
print(B[0, 1])
print(B[:, 0], (B[:, 0]).shape)  # shape = (3,)
print(B[1:3, :2])

# ------------------------

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a)
print(a.transpose())
print(a.transpose().transpose())  # a == a.transpose().transpose()

print(a.dot(b))
print((a.dot(b)).transpose())
print((b.transpose()).dot(a.transpose()))

# ------------------------

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(np.diag(a))

# ------------------------

# LGS - Lösung mit Gauß
A = np.array([
    [-1, 1, 1],
    [0, -3, -2],
    [0, 0, 4],
])

b = np.array([0, 5, 3])

print(solve_triangular(A, b))

# ------------------------

print(np.identity(5))

A = np.array([
    [-1, 1, 1],
    [0, -3, -2],
    [0, 0, 4],
])

# Die inv-Methode ist nicht stabil, also nicht verwenden.
# B = np.linalg.inv(A)
# B = np.linalg.solve(A, np.identity(n))

# Es sei denn, A ist orthogonal
# A ^ -1 = A ^ T

# ------------------------

# LGS - Lösung mit Gauß
A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4],
])

b = np.array([0, 5, 3])

print(b.shape)
# print(b.shape[0])
x, = b.shape
print(x)

# ------------------------

# LGS - Lösung mit Gauß
A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
])

b = np.array([0, 5, 3])


print("Lösung mit Gauß:")
print(np.linalg.solve(A, b).round().astype(int))  # [-1 -4  3]


print("------------------------")

A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
])

print(A[0])
print(A[0].copy())

print("------------------------")

A = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
], dtype='float')


x = np.array([0, 5, 3])

b = np.dot(A, x)
print(b)

print(A[2][2])


print("------------------------")

M = np.array([
    [-1, 1, 1],
    [1, -3, -2],
    [5, 1, 4]
])

# if np.array_equal(M[i],np.transpose(M[i])):
print(M[1])
print(np.transpose(M[1]))
print(np.array_equal(M[1],np.transpose(M[1])))


print("------------------------")

M = np.array([
    [1, 4, 3],
    [4, 2, 6],
    [3, 6, 3]
])

(n, m) = M.shape

for i in range (n):
    for j in range(m):
        if M[i][j]!=M[j][i]:
            print("Kein symetrisches Matrix")
print("ist symetrisches Matrix")

print("------------------------")

print(np.zeros(4 * 10))
print(type(np.zeros(4 * 10)))

print("------------------------")

M = np.array([
    [1, 0],
    [0, 1]
])

print(np.linalg.cholesky(M))

print("------------------------")

M = np.array([
    [5, 4],
    [3, 4]
])

print(np.linalg.det(M))

print("------------------------")

M = np.array([
    [1, 1, 3, 1],
    [3, 1, 1, 2],
    [4, 2, 4, 3],
    [2, 1, -2, 1]
])

print(np.linalg.matrix_rank(M))
print(np.linalg.det(M))

print("------------------------")

M = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

ew,ev = np.linalg.eig(M)

print(ew)

print(ev)

print("------------------------")

A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])


B = np.array([
    [-1],
    [-2],
    [-3]
])

print(A@B)


print("------------------------")

A = np.array([
    [4, 3],
    [2, 5]
])

ew,ev = np.linalg.eig(A)

print(ew)

print(ev)

print("------------------------")

A = np.array([
    [1, 2, 2],
    [2, 1, 2],
    [1, 1, 3]
])


ew,ev = np.linalg.eig(A)

print(ew)

print(ev)

print("------------------------")

A = np.array([
    [5, 0],
    [0, -5]
])

ew,ev = np.linalg.eig(A)

print(ew)

print(np.abs(ew[0]) * ev)

print("------------------------")

A = np.array([
    [1, 2, 4, 8],
    [2, 1, 6, 8],
    [4, 6, 3, 6],
    [8, 8, 6, 8]
])


ew,ev = np.linalg.eig(A)

print(ew)

print(ev)


print("------------------------")

A = np.array([
    [-2, 0, 0],
    [-2, -2, 0],
    [2, 0, -2]
])


ew,ev = np.linalg.eig(A)

print(ew)

print(ev)

inv = np.linalg.inv(A) 
print(inv)
print(np.dot(A, inv))


print("------------------------")

A = np.array([
    [6, -5, 8],
    [6, 5, 8],
    [6, -5, 8],
    [6, 5, 8]
])


U, s, Vt = np.linalg.svd(A, full_matrices=True)
print(U, '\n--------------------------')
print(s, '\n--------------------------')
print(Vt, '\n--------------------------')

print("------------------------")

A = np.array([
    [6, -5, 8],
    [6, 5, 8],
    [6, -5, 8]
])


U, s, Vt = np.linalg.svd(A, full_matrices=True)
print(U, '\n--------------------------')
print(s, '\n--------------------------')
print(Vt, '\n--------------------------')

print(np.linalg.det(A))

print("------------------------")

A = np.array([
    [-2, 0, 0],
    [-2, -2, 0],
    [2, 0, -2]
])


U, s, Vt = np.linalg.svd(A, full_matrices=True)
print(U, '\n--------------------------')
print(s, '\n--------------------------')
print(Vt, '\n--------------------------')

print(np.linalg.det(A))


print("------------------------")

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A)
print(A.shape)
print(A.shape[0])

print("------------------------")

print(np.random.rand(4))

print("------------------------")

T = np.array([[0.5, 0.25, 0.25], [0.5, 0.0, 0.5], [0.25, 0.25, 0.5]])

vector = np.random.rand(T.shape[0])

print(vector.dot(M.dot(vector)))
print(M.dot(vector))

print("------------------------")

A = np.array([
    [9, 9],
    [9, 3]
])

evalue,evector = np.linalg.eigh(A)

print(evalue)
print(evector)

print(np.linalg.norm(evector[:,0]))

# print(np.abs(ew[1]) * ev)

print("------------------------")