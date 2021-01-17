import numpy as np

x = np.array([1, 2, 3, 4])

vm_1 = np.vander(x)
print(vm_1)

vm_2 = np.vander(x, increasing=True)
print(vm_2)

##########################################
# LGS

A = vm_2
b = [4, 1, 5, 9]

print(np.linalg.solve(A, b))

