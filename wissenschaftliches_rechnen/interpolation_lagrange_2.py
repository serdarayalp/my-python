import numpy as np
from scipy.interpolate import lagrange

x = np.array([1, 2, 3])
y = np.array([1, 2, 2])

poly = lagrange(x, y)
print(poly)
