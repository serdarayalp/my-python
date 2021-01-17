
import numpy as np
import matplotlib.pyplot as plt

# C={(2,2),(3,6),(4,5),(5,5),(6,6)}
x = np.array([2., 3., 4., 5., 6.])
y = np.array([2., 6., 5., 5., 6.])

V = np.vander(x, increasing=True)
print('V matrix')
print(V)

a = np.linalg.solve(V, y)
print('Polynomial coefficients:')
print(a)

# plt.plot(x, y)
plt.plot(x, y, 'ro')

plt.show()
