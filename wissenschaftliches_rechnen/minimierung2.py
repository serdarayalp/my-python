import numpy as np

#A = np.array(([3,2,7,2],[5,5,2,7],[9,1,1,7],[1,3,2,9]),dtype=np.float32)
#A = np.array(([5,9,1,1],[9,5,7,8],[6,3,8,1],[9,7,2,5]),dtype=np.float32)
#A = np.array(([4,1,4,6],[7,5,9,3],[3,2,9,4],[5,5,2,7]),dtype=np.float32)
#A = np.array(([1,4,4,3],[1,5,6,6],[3,8,3,4],[2,8,2,4]),dtype=np.float32)

A = np.array([
    [2, 3, 1, 7],
    [3, 5, 4, 2],
    [6, 9, 2, 1],
    [6, 1, 2, 2]
])


print("Ausgangsmatrix:")
print(A)

# Singulärwertzerlegung
a, svals, pcs = np.linalg.svd(A,full_matrices=False)

print("Singulärwerte")
print(svals)

print("VT")
print(pcs)

v = np.transpose(pcs)
x = v[:,3]

print("Bester Vektor: x=")
print(x)
print(np.linalg.norm(x))

z = np.dot(A,x)


print("Norm: ||Ax|| = ")
print(np.linalg.norm(z)) 