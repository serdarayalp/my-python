# importing the modules
import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
x = np.arange(1, 11)
print(x)

y = x * x
print(y)

# plotting
plt.title("Line graph")

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.plot(x, y, color="red")
plt.show()
