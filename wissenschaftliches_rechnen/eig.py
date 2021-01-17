import numpy as np

A = np.array([
    [9, 9],
    [9, 3]
])

evalue,evector = np.linalg.eig(A)

print(evalue)
print(evector)

# Norm der Eigenvektoren
print(np.linalg.norm(evector[:,0]))
print(np.linalg.norm(evector[:,1]))

# print(evalue[0])
print(np.abs(evalue[0]) * evector[:,0])
print(np.abs(evalue[1]) * evector[:,1])

print("------------------------")

A = np.array([
    [5, 0],
    [0, -5]
])


evalue,evector = np.linalg.eig(A)

print(evalue)
print(evector)

# Norm der Eigenvektoren
print(np.linalg.norm(evector[:,0]))
print(np.linalg.norm(evector[:,1]))

# print(evalue[0])
print(np.abs(evalue[0]) * evector[:,0])
print(np.abs(evalue[1]) * evector[:,1])
