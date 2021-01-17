import numpy as np

A = np.array([
    [2, 3, 1],
    [3, 5, 4],
    [6, 9, 2],
    [6, 1, 2]
])


U, s, Vt = np.linalg.svd(A, full_matrices=True)

print(U)
print(s)
print(Vt)

print("------------------------")

V = np.transpose(Vt)
print(V)

print("------------------------")

print(A.dot(V[:, 0]))
print(A.dot(V[:, 1]))
print(A.dot(V[:, 2]))
# print(A.dot(V[:, 3]))

print("------------------------")

print(U)
print(s)
print(Vt)

# print(Vt[0, :])
# print(Vt[1, :])
print(np.dot(Vt[0, :],Vt[1, :]))



