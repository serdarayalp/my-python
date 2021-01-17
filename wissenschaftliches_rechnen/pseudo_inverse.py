import numpy as np

A = np.random.randn(9, 6)
print(A)

print("------------------------")

B = np.linalg.pinv(A)
print(B)

print("------------------------")

# The following example checks that:
# ----- A * A+ * A == A 
# ----- A+ * A * A+ == A+
print(np.allclose(A, np.dot(A, np.dot(B, A))))
print(np.allclose(B, np.dot(B, np.dot(A, B))))

print("------------------------")

A = np.array([
    [2, 3, 6],
    [-2, 3, -4],
])
