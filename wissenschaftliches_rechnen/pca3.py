import numpy as np
from sklearn.decomposition import PCA

k = 1 # target dimension(s)
pca = PCA(k) # Create a new PCA instance

data = np.array([
    [4],
    [5],
    [5]
])

data = data - data.mean(axis=0) # Center data points
print(data)
