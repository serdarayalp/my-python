import numpy as np
import matplotlib.pyplot as plt

# Liste mit Temperaturwerten in Celsius
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]

# wir erzeugen nun ein eindimensionales NumPy-Array
C = np.array(cvalues)
print(C, type(C))

# Werte in Grad Fahrenheit ((0 °C × 9/5) + 32 = 32 °F) - NumPy-Lösung
print((C * (9 / 5)) + 32)
print(C)

# Werte in Grad Fahrenheit ((0 °C × 9/5) + 32 = 32 °F) - Python-Lösung
fValues = [cv * 9/5 + 32 for cv in cvalues]
print(fValues)

plt.plot(C)
plt.show()
