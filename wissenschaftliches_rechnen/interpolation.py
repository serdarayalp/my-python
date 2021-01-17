import numpy as np
import scipy.linalg as spl
import scipy.interpolate as spi

"""
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0):

    Gibt gleichmäßig verteilte Zahlen über ein angegebenes Intervall zurück.
    Gibt num gleichmäßig verteilte Stichproben zurück, berechnet über das Intervall [start, stop].
    Der Endpunkt des Intervalls kann optional ausgeschlossen werden.
"""
interp_x = np.linspace(-5, 5, 13)

interp_y = 1 / (1 + interp_x**2)

V = np.vander(interp_x, 13)

p = spl.solve(V, interp_y)
print(p)