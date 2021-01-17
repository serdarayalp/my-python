import numpy as np
from sklearn.decomposition import PCA

k = 1 # target dimension(s)
pca = PCA(k) # Create a new PCA instance

data = np.array([
    [0, 1, -1],
    [2, -1, -1]
])

print("Data: ", data)
print("Reduced: ", pca.fit_transform(data)) # fit and transform


data = data - data.mean(axis=0) # Center data points
print("Centered Matrix: ", data)


cov = np.cov(data.T) / data.shape[0] # Get covariance matrix
print("Covariance matrix: ", cov)


v, w = np.linalg.eig(cov)


idx = v.argsort()[::-1] # Sort descending and get sorted indices
v = v[idx] # Use indices on eigv vector
w = w[:,idx] # 

print("Eigenvalue vektoru: ", v)
print("Eigenvektorler: ", w)

print("Ergebnis: ", data.dot(w[:, :k]))
# Get the dot product of w with the first K columns of eigenvector matrix
# (a.k.a) projection matrix



