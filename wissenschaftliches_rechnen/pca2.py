import numpy as np

from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig


# define a matrix
A = np.array([
    [0, 2],
    [1, -1],
    [-1, -1]
])

# print(A)
# calculate the mean of each column
M = mean(A.T, axis=1)
# print(M)
# center columns by subtracting column means
C = A - M
# print(C)
# calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)

# eigendecomposition of covariance matrix
values, vectors = eig(V)
print(vectors)
print(values)
# project data
P = vectors.T.dot(C.T)
print(P.T)