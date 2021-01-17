import numpy as np

v1 = np.array([3,9,3])
v2 = np.array([3,2,9])
v3 = np.array([4,5,5])

#v1 = np.array([2,3,1])
#v2 = np.array([5,8,1])
#v3 = np.array([9,5,9])

v = v1 + v2 + v3
print(v)

v = v / 3
print(v)

print(v1-v)
print(v2-v)
print(v3-v)