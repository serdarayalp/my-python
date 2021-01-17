import pandas as pd
import numpy as np

# Let's take this dataset
a = [[0,2],[1,-1],[-1,-1]]
b = ['X','Y']
dat = pd.DataFrame(a,columns = b)

print(dat)

#Let's create the covariance matrix here.
# An intuitive reason as to why we're doing this is to capture the variance of the entire dataset
C = np.cov(dat.T)
eigenvalues, eigenvectors = np.linalg.eig(C)

# Let's sort them now
idx = eigenvalues.argsort()[::-1]
eigenvalues= eigenvalues[idx]
eigenvectors = eigenvectors[:,idx]

# Let's check them again

print(eigenvalues)

print(eigenvectors)

