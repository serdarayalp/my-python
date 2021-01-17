import numpy as np

"""
Prinzipiell gibt es drei verschiedene Formen von Broadcasting:
    * in horizontaler Richtung
    * in vertikaler Richtung
    * in horizontaler und vertikaler Richtung

Broadcasting bei zwei Arrays in NumPy erfolgt nach folgenden Regeln:
--------------------------------------------------------------------
Regel 1
Falls die beiden Arrays in ihrer Anzahl von Dimensionen sich unterscheiden, wird die Shape des Arrays, 
das weniger Dimensionen hat, mit Einsen von der linken Seite aus
aufgefüllt.

Regel 2
Falls die Shapes von zwei Arrays an einer Shape-Position nicht übereinstimmen, wird die Shape desjenigen 
Arrays angepasst, die eine 1 enthält. Der Wert wird dann auf den Wert des anderen Arrays erhöht.

Regel 3
Falls in irgendeiner Dimension die Größen unterschiedlich sind und keine von beiden gleich 1 ist, 
wird ein Fehler erhoben.
"""

v = np.array([3, 5, 1])
x = 4  # = np.array([4, 4, 4])
print(v * x)

# Zeilenweises Broadcasting

A = np.array([[11, 12, 13],
              [21, 22, 23],
              [31, 32, 33]])

B = np.array([1, 2, 3])

print(A.shape)
print(B.shape)

print("Multiplikation mit Broadcasting: ")
print(A * B)
print("... und nun die Addition mit Broadcasting: ")
print(A + B)

print("-------------------------------------------------------")

B = np.array([1, 2, 3])
print("Die Shape von B: ", B.shape)

"""
Regel 1
Falls die beiden Arrays in ihrer Anzahl von Dimensionen sich unterscheiden, wird die Shape des Arrays, 
das weniger Dimensionen hat, mit Einsen von der linken Seite aus aufgefüllt.

Regel 2
Falls die Shapes von zwei Arrays an einer Shape-Position nicht übereinstimmen, wird die Shape desjenigen 
Arrays angepasst, die eine 1 enthält. Der Wert wird dann auf den Wert des anderen Arrays erhöht.

"""
# Anwendung der Regel 1:
B = B[np.newaxis, :]
print("Shape nach Anwendung der ersten Regel: ", B.shape)
B = np.tile(B, (3, 1))
print("Shape nach Anwendung der zweiten Regel: ", B.shape)
print(B)


B = np.array([1, 2, 3])
B = B.reshape((B.shape[0], 1))  # Alternative : B[:, np.newaxis]
print(B)


A = np.array([[11, 12, 13],
              [21, 22, 23],
              [31, 32, 33]])
B = np.array([1, 2, 3])

print(A * B)
print(A * B[:, np.newaxis])


# Broadcasting von zwei eindimensionalen Arrays

A = np.array([10, 20, 30])
B = np.array([1, 2, 3])

# wir richten A auf:
A = A.reshape(A.shape[0], 1)
print(A)
# nun können wir das Broadcasting durchführen:
print(A * B)
