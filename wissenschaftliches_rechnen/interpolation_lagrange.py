import numpy as np

# conda install -c conda-forge matplotlib
# sudo apt-get install python3-distutils
import matplotlib.pyplot as plt


def intpoly(x, y):
    V = np.vander(x, len(x))
    a = np.linalg.solve(V, y)
    return np.poly1d(a)


x = np.linspace(0, 4.0, 13)
y = np.sin(x * np.pi * 2.5) * np.exp(-x ** 2 / 8.0)

for k in range(1, 4):
    plt.subplot(1, 3, k)
    plt.plot(x, y, 'ko', zorder=0)

    for i in range(0, len(x) - k, k):
        p = intpoly(x[i:i + k + 1], y[i:i + k + 1])
        tx = np.linspace(x[i], x[i + k], 20)
        ty = p(tx)
        plt.plot(tx, ty, '-')

    plt.grid(True)
    plt.xlim(-0.1, 4.1)
    plt.ylim(-1.1, 1.1)
    plt.gca().set_aspect('equal')

plt.show()
