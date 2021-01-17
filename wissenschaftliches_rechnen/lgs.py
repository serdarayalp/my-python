import numpy as np

A = [[-1,1,-2], [0,3,-1], [2,0,1]]
b = [-5, 3, 5]

# Pseudo-Inverse
B = np.linalg.pinv(A)

print(np.linalg.solve(A, b)) # [1. 2. 3.]

print("------------------------")

# Ax=b, dann x = A+ * b
print(B.dot(b))

print("------------------------")

print(A)
print(B)
print(np.matmul(A, B))
