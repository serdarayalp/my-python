import numpy as np

x = np.array([1, 2, 3, 4])

vm = np.vander(x, increasing=True)
print(vm)

A = vm

print("-------------- V")
print(A)

print("-------------- L = V ^ 1")
print(np.linalg.inv(A))

b = [4, 1, 5, 9]

##########################################
# LGS
# print(np.linalg.solve(A, b))
