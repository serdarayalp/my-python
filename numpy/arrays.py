import numpy as np

"""
Die Syntax von arange:

arange([start,] stop[, step], [, dtype=None])

arange liefert gleichmäßig verteilte Werte innerhalb eines gegebenen Intervalles zurück. 
Die Werte werden innerhalb des halb-offenen Intervalles [start, stop) generiert. Wird diese Funktion 
mit Integer-Werten benutzt, ist sie beinahe äquivalent zu der built-in Python-Funktion range. arange liefert 
jedoch ein ndarray zurück, während range einen Listen-Iterator zurückliefert. Falls der start-Parameter 
nicht übergeben wird, wird start auf 0 gesetzt. Das Ende des Intervalls wird durch den Parameter stop bestimmt. 
Üblicherweise wird das Intervall diesen Wert nicht beinhalten, außer in den Fällen, in denen step keine 
Ganzzahl ist und floating-point-Effekte die Länge des Ausgabearrays beeinflussen. Der Abstand zwischen zwei 
benachbarten Werten des Ausgabearrays kann mittels des optionalen Parameters step gesetzt werden. 
Der Default-Wert für step ist 1.

Falls ein Wert für step angegeben wird, kann der start-Parameter nicht mehr optional sein, d.h. er muss dann 
auch angegeben werden.

Der Type des Ausgabearrays kann mit dem Parameter dtype bestimmt werden. Wird er nicht angegeben, wird der 
Typ automatisch aus den übergebenen Eingabewerten ermittelt.
"""

print(np.arange(15))  # [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]

a = np.arange(1, 7)
print(a)  # [1 2 3 4 5 6]

# im Vergleich dazu nun range:
x = range(1, 7)
print(x)  # x ist ein Iterator, und der Wert ist range(1, 7)
print(list(x))  # [1, 2, 3, 4, 5, 6]

# weitere arange-Beispiele:
x = np.arange(7.3)  # [0. 1. 2. 3. 4. 5. 6. 7.]
print(x)

x = np.arange(0.5, 6.1, 0.8)  # [0.5 1.3 2.1 2.9 3.7 4.5 5.3]
print(x)

x = np.arange(0.5, 6.1, 0.8, np.int)  # [0 1 2 3 4 5 6]
print(x)


print("-------------------------------------------------------")

"""
Die Syntax von linspace:

linspace(start, stop, num=50, endpoint=True, retstep=False)

linspace liefert ein ndarray zurück, welches aus 'num' gleichmäßig verteilten Werten aus dem geschlossenen 
Interval ['start', 'stop'] oder dem halb-offenen Intervall ['start', 'stop') besteht. Ob ein geschlossenes 
oder ein halb-offenes Intervall zurückgeliefert wird, hängt vom Wert des Parameters endpoint ab. stop ist der 
letzte Wert des Intervalls, falls endpoint nicht auf False gesetzt ist. Die Schrittweite ist unterschiedlich, 
je nachdem, ob endpoint True oder False ist:

 Falls der Parameter 'retstep' gesetzt ist, wird die Funktion auch den Wert des Abstandes zwischen zwei 
 benachbarten Werten des Ausgabearrays zurückliefern.
"""

# 50 Werte (Defaut) zwischen 1 und 10:
print(np.linspace(1, 10))

# 7 Werte zwischen 1 und 10:
print(np.linspace(1, 10, 7))

# jetzt ohne Endpunkt:
print(np.linspace(1, 10, 7, endpoint=False))

print("-------------------------------------------------------")

samples, spacing = np.linspace(1, 10, retstep=True)
print(spacing)

samples, spacing = np.linspace(1, 10, 5, endpoint=True, retstep=True)
print(samples, spacing)

samples, spacing = np.linspace(1, 10, 5, endpoint=False, retstep=True)
print(samples, spacing)


print("-------------------------------------------------------")

x = np.array(42)
print("x: ", x)
print("Der Typ von x: ", type(x))
print("Die Dimension von x:", np.ndim(x))

print("-------------------------------------------------------")

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
V = np.array([3.4, 6.9, 99.8, 12.8])

print("F: ", F)
print("V: ", V)

print("Typ von F: ", F.dtype)
print("Typ von V: ", V.dtype)

print("Dimension von F: ", np.ndim(F))
print("Dimension von V: ", np.ndim(V))

print("-------------------------------------------------------")

A = np.array([[3.4, 8.7, 9.9],
              [1.1, -7.8, -0.7],
              [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)
print(A[0, 0])
print(A[0, 1])
print(A[0, 2])
print(A[1, 0])
print(A[1, 1])
print(A[1, 2])

print("-------------------------------------------------------")

x = np.array([[67, 63, 87],
              [77, 69, 59],
              [85, 87, 99],
              [79, 72, 71],
              [63, 89, 93],
              [68, 92, 78]])

print(np.shape(x))
print(x.shape)

x.shape = (3, 6)
print(x)

x.shape = (2, 9)
print(x)

x = np.array(11)
print(np.shape(x))


B = np.array([[[111, 112], [121, 122]],
              [[211, 212], [221, 222]],
              [[311, 312], [321, 322]]])
print(B.shape)

print("-------------------------------------------------------")

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# Ausgabe des ersten Elements von F
print(F[0])
# Ausgabe letztes Element von F
print(F[-1])


A = np.array([[3.4, 8.7, 9.9],
              [1.1, -7.8, -0.7],
              [4.1, 12.3, 4.8]])
print(A[1][0])
print(A[1, 0])

B = np.array([[[111, 112], [121, 122]],
              [[211, 212], [221, 222]],
              [[311, 312], [321, 322]]])
print(B[0][1][0])

print("-------------------------------------------------------")

S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])

print("-------------------------------------------------------")

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]])

ergebnis = A[:3, 2:]
print(ergebnis, ergebnis.shape)


print("-------------------------------------------------------")

print(A[3:, :])

print("-------------------------------------------------------")

print(A[:, 4:])

print("-------------------------------------------------------")

ergebnis = np.arange(28)
print(ergebnis, type(ergebnis), np.ndim(ergebnis),
      np.shape(ergebnis), ergebnis.shape)

# Die reshape-Funktion benutzen wir, um ein eindimensionales Array in ein zweidimensionales zu wandeln.
X = np.arange(28).reshape(4, 7)
print(X)

print(X[::, ::])
print(X[::2, ::])
print(X[1::2, ::])

print(X[::, ::3])
print(X[::2, ::3])

print("-------------------------------------------------------")

A = np.array(
    [[[45, 12, 4], [45, 13, 5], [46, 12, 6]],
     [[46, 14, 4], [45, 14, 5], [46, 11, 5]],
     [[47, 13, 2], [48, 15, 5], [52, 15, 1]]])

ergebnis = A[1:3, 0:2]
print(ergebnis, np.shape(ergebnis))  # equivalent to A[1:3, 0:2, :]
"""
[
    [[46 14  4][45 14  5]]
    [[47 13  2][48 15  5]]
]
"""

print("-------------------------------------------------------")

"""
Während der Teilbereichsoperator bei Listen und Tupel neue Objekte erzeugt, generiert er bei NumPy nur 
eine Sicht ("view") auf das Originalarray. Dadurch erhalten wir eine andere Möglichkeit, 
das Array anzusprechen, oder besser einen Teil des Arrays. Daraus folgt, dass wenn wir etwas in einer 
Sicht verändern, wir auch das Originalarray verändern.
"""

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A[2:6]
print(S)
S[0] = 22
S[1] = 23
print(A)

print("-------------------------------------------------------")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = lst[2:6]
lst2[0] = 22
lst2[1] = 23
print(lst)

print("-------------------------------------------------------")

"""
Will man prüfen, ob zwei Arrays auf den gleichen Speicherbereich zugreifen, 
so kann man die Funktion "np.may_share_memory" benutzen:

np.may_share_memory(A, B)
"""

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B = A[2:5]
print(np.may_share_memory(A, B))

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B1 = A[::2]
B2 = A[1::2]
print(np.may_share_memory(B1, B2))

# Dreidimensionale Arrays

X = np.array(
    [[[3, 1, 2], [4, 2, 2]],
     [[-1, 0, 1], [1, -1, -2]],
     [[3, 2, 2], [4, 4, 3]],
     [[2, 2, 1], [3, 1, 3]]])

print(X.shape)
print(type(X.shape))
print(X.shape[0])
print(X.shape[1])
print(X.shape[2])


print("Dimension 0 with size ", X.shape[0])
for i in range(X.shape[0]):
    print(f"\nAusgabe von X[{i:1},:,:]")
    print(X[i, :, :])

print("\nDimension 1 with size ", X.shape[1])
for i in range(X.shape[1]):
    print(f"\nAusgabe von X[:,{i:1},:]")
    print(X[:, i, :])

print("\nDimension 2 with size ", X.shape[2])
for i in range(X.shape[2]):
    print(f"\nAusgabe von X[:,:,{i:1}]")
    print(X[:, :, i])


# Arrays mit Nullen und Einsen

"""
Arrays können auf zwei Arten mit Nullen und Einsen initialisiert werden. Die Methode ones(t) hat als 
Parameter ein Tupel t mit der Shape des Arrays und erzeugt entsprechend ein Array mit Einsen. Defaultmäßig 
wird es mit Float-Einsen gefüllt. Wenn man Integer-Einsen benötigt, kann man den optionalen Parameter dtype 
auf int setzen:
"""

E = np.ones((2, 3))
print(E)

F = np.ones((3, 4), dtype=int)
print(F)

Z = np.zeros((2, 4))
print(Z)

Z = np.zeros((2, 4), dtype=int)
print(Z)

x = np.array([2, 5, 18, 14, 4])
E = np.ones_like(x)
print(E)

Z = np.zeros_like(x)
print(Z)

print("-------------------------------------------------------")

# Arrays kopieren

"""
numpy.copy(obj, order='K')
obj.copy(order='C')

    obj 	array_like input data.
    order 	The possible values are {'C', 'F', 'A', 'K'}. This parameter controls the memory layout of the copy. 
            'C' means C-order, 'F' means Fortran-order, 'A' means 'F' if the object 'obj' is Fortran contiguous, 
            'C' otherwise. 'K' means match the layout of 'obj' as closely as possible.

            Um den Parameter order zu verstehen, gehen wir noch kurz auf den Begriff "zusammenhängend" 
            (englisch "contiguous") ein. Die Speicherstruktur eines Arrays wird als zusammenhängend bezeichnet,
             wenn die Speicherung eines Arrays entweder C-zusammenhängend (C_CONTIGUOUS) oder 
             Fortran-zusammenhängend (F_CONTIGUOUS) erfolgt. 

            F_CONTIGUOUS:
            Wird ein Array spaltenweise abgespeichert, so bezeichnet man dies als F-zusammenhängend.
            
            C_CONTIGUOUS:
            Wird ein Array zeilenweise abgespeichert, spricht man von C-zusammenhängend.
"""

M = np.array([[11, 12, 13, 14],
              [21, 22, 23, 24],
              [31, 32, 33, 34]], order='F')

copied1 = np.copy(M)  # default-Order = K
copied2 = M.copy()  # default-Order = C

print(M)
print(M.flags['C_CONTIGUOUS'])
print(M.flags['F_CONTIGUOUS'])

print(copied1.flags['C_CONTIGUOUS'])
print(copied2.flags['C_CONTIGUOUS'])

print("-------------------------------------------------------")

T = M.transpose()
print(M.flags['C_CONTIGUOUS'])
print(T.flags['C_CONTIGUOUS'])
print(T.strides, M.strides)

print("-------------------------------------------------------")

T = copied1.transpose()

print(copied1.flags['C_CONTIGUOUS'])
print(T.flags['C_CONTIGUOUS'])

print(T.strides, copied1.strides)


print("-------------------------------------------------------")

m = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9]], np.dtype=int32, order='C')

"""
This array is stored in memory as 40 bytes, one after the other (known as a contiguous block of memory). 
The strides of an array tell us how many bytes we have to skip in memory to move to the next position along a 
certain axis. For example, we have to skip 4 bytes (1 value) to move to the next column, but 20 bytes (5 values) 
to get to the same position in the next row. As such, the strides for the array x will be (20, 4).
"""

print(m.strides)


m2 = np.array([[0, 1, 2, 3, 4],
               [5, 6, 7, 8, 9]], dtype=np.int32, order='F')

print(m2.strides)


m = np.array(
    [[[3, 1, 2], [4, 2, 2]],
     [[-1, 0, 1], [1, -1, -2]],
     [[3, 2, 2], [4, 4, 3]],
     [[2, 2, 1], [3, 1, 3]]])

print(m.strides)

print("-------------------------------------------------------")


# Identitäts-Array

# identity(n, dtype=None)

print(np.identity(4, dtype=np.int32))
print(np.identity(4, dtype=int))

"""
eye(N, M=None, k=0, dtype=float)

Parameter 	Bedeutung
-----------------------------------------------------------------------------------------------
N 	        Eine Integer-Zahl, welche die Anzahl der Zeilen des Ausgebearrays bestimmt.
M 	        Eine Integer-Zahl, welche die Spalten des Ausgabearrays bestimmt. Falls dieser Parameter nicht gesetzt ist oder None ist, wird er per Default auf 'N' gesetzt.
k 	        Mit 'k' wird die Position der Diagonalen gesetzt. Der Default ist 0. 0 bezeichnet die Hauptdiagonale. Ein positiver Wert bezeichnet eine obere Diagonale und ein negativer Wert eine untere Diagonale.
dtype 	    Ein optionales Argument, welches den Datentyp des Ergebnisses definiert. Der Default ist 'float'.
"""
print(np.eye(5, 8, k=-1, dtype=int))
print(np.eye(5, 8, k=0, dtype=int))
print(np.eye(5, 8, k=1, dtype=int))
print(np.eye(5, 8, k=2, dtype=int))
