import numpy as np

# A = np.array(([9,5,7,8],[8,5,8,1],[9,7,4,7],[7,6,2,6]))
A = np.array([
    [2, 3, 1, 7],
    [3, 5, 4, 2],
    [6, 9, 2, 1],
    [6, 1, 2, 2]
])

m = np.mean(A, axis = 0)

for i in range(A.shape[0]):
    A[i,:] = A[i,:] - m

U, s, Vt = np.linalg.svd(A, full_matrices=True)

x = Vt[:,3]

print("x:")
print(x)

print("Norm - x: ")
print(np.linalg.norm(x))

print("Ax: ")
Ax = np.dot(A,x)
print(Ax)

print("Norm - Ax: ")
print(np.linalg.norm(Ax)) 