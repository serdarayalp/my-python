# importing the modules
import numpy as np

# pyplot stellt eine prozedurale Schnittstelle zur objektorientierten Plot-Bibliothek von Matplotlib
# zur Verfügung. Die Kommandos von pyplot sind so gewählt, dass sie sowohl in den Namen als auch in ihren
# Argumenten MATLAB ähnlich sind.
import matplotlib.pyplot as plt

"""
linspace

Die Syntax von linspace:
    linspace(start, stop, num=50, endpoint=True, retstep=False)

linspace liefert ein ndarray zurück, welches aus 'num' gleichmäßig verteilten Werten aus dem geschlossenen 
Interval ['start', 'stop'] oder dem halb-offenen Intervall ['start', 'stop') besteht. Ob ein geschlossenes oder 
ein halb-offenes Intervall zurückgeliefert wird, hängt vom Wert des Parameters endpoint ab. stop ist der letzte 
Wert des Intervalls, falls endpoint nicht auf False gesetzt ist. Die Schrittweite ist unterschiedlich, 
je nachdem, ob endpoint True oder False ist:
"""

# 50 Werte (Defaut) zwischen 1 und 10:
print(np.linspace(1, 10))

# 7 Werte zwischen 1 und 10:
print(np.linspace(1, 10, 7))

# jetzt ohne Endpunkt:
print(np.linspace(1, 10, 7, endpoint=False))

"""
Falls der Parameter 'retstep' gesetzt ist, wird die Funktion auch den Wert des Abstandes zwischen 
zwei benachbarten Werten des Ausgabearrays zurückliefern. Die Funktion liefert also ein Tupel ('samples', 'step') 
zurück:
"""

samples, spacing = np.linspace(1, 10, retstep=True)
print(spacing)

samples, spacing = np.linspace(1, 10, 5, endpoint=True, retstep=True)
print(samples, spacing)

samples, spacing = np.linspace(1, 10, 5, endpoint=False, retstep=True)
print(samples, spacing)


