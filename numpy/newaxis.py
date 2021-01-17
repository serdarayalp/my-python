import numpy as np

A = np.array([1, 2, 3, 4])
B = np.array([1, 2, 3, 4])


print(A)
print(A.shape)
A = A[np.newaxis, :]
print(A)
print(A.shape)


print(B)
print(B.shape)
B = B[:, np.newaxis]
print(B)
print(B.shape)
