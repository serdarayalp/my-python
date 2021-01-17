import numpy as np

# Wenn mindestens zwei Stützstellen den selben Wert haben,
# ist die Systemmatrix des resultierenden Gleichungssystems singulär.

x = np.array([2, 2, 3, 4])

vm = np.vander(x, increasing=True)
print(vm)

print(vm)

print(np.linalg.inv(vm))

