# importing the modules
import numpy as np

# pyplot stellt eine prozedurale Schnittstelle zur objektorientierten Plot-Bibliothek von Matplotlib
# zur Verfügung. Die Kommandos von pyplot sind so gewählt, dass sie sowohl in den Namen als auch in ihren
# Argumenten MATLAB ähnlich sind.
import matplotlib.pyplot as plt

# plt.plot([-1, -4.5, 16, 23, 15, 59]) # default Formatparameter "b-"
# plt.plot([-1, -4.5, 16, 23, 15, 59], "b_")
# plt.show()

"""
Die folgenden Zeichen werden in einem Formatstring akzeptiert, um den Linienstil oder die Marker zu steuern:

Zeichen       Beschreibung
=============================================
'-' (Bindestrich) durchgezogene Linie
'--' (zwei Bindestriche) gestrichelte Linie
'-.' Strichpunkt-Linie
':' punktierte Linie
'.' Punkt-Marker
',' Pixel-Marker
'o' Kreis-Marker
'v' Dreiecks-Marker, Spitze nach unten
'^' Dreiecks-Marker, Spitze nach oben
'<' Dreiecks-Marker, Spitze nach links
'>' Dreiecks-Marker, Spitze nach rechs
'1' tri-runter-Marker
'2' tri-hoch-Marker
'3' tri-links Marker
'4' tri-rechts Marker
's' quadratischer Marker
'p' fünfeckiger Marker
'*' Stern-Marker
'h' Sechseck-Marker1
'H' Sechseck-Marker2
'+' Plus-Marker
'x' x-Marker
'D' rautenförmiger Marker
'd' dünner rautenförmiger Marker
'|' Marker in Form einer vertikalen Linie
'_' Marker in Form einer horizontalen Liniw



Die folgenden Farbabkürzungen sind möglich:

==================
Zeichen    Farbe
==================
'b' blau
'g' grün
'r' rot
'c' cyan
'm' magenta
'y' gelb
'k' schwarz
'w' weiß

"""


# die X-Werte:
days = list(range(0, 22, 3))
print(days)

# die Y-Werte:
celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]

# plt.plot(days, celsius_values)
plt.xlabel('Day')
plt.ylabel('Degrees Celsius')
# plt.show()

# ----------------------------------------------------

# Wir können eine beliebige Anzahl von (x, y, format)-Gruppen in einer Plot-Funktion spezifizieren.

days = list(range(1, 9))

celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]

plt.xlabel('Day')
plt.ylabel('Degrees Celsius')

"""
plt.plot(days, celsius_min,
         days, celsius_min, "oy",
         days, celsius_max,
         days, celsius_max, "or")
"""

# plt.show()

# ----------------------------------------------------

days = list(range(1, 9))

celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]

plt.xlabel('Day')
plt.ylabel('Degrees Celsius')

"""
plt.plot(days, celsius_min,
         days, celsius_min, "oy",
         days, celsius_max,
         days, celsius_max, "or")
"""

print("The current limits for the axes are:")
# Ruft man axis ohne Argumente auf, liefert sie den aktuellen Wertebereich einer Achse zurück.
print(plt.axis())

print("We set the axes to the following values:")
xmin, xmax, ymin, ymax = 0, 10, 0, 45
print(xmin, xmax, ymin, ymax)

# plt.axis([xmin, xmax, ymin, ymax])
# plt.show()

# ------------------------------------------------

# linspace(start, stop, num=50, endpoint=True, retstep=False)
X = np.linspace(0, 2 * np.pi, 50, endpoint=True)

F = np.sin(X)

# plt.plot(X, F)

startx, endx = -0.1, 2*np.pi + 0.1
starty, endy = -1.1, 1.1
# plt.axis([startx, endx, starty, endy])

# plt.show()

# ------------------------------------------------

X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)

F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)

startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3.1, 3.1
# plt.axis([startx, endx, starty, endy])

# plt.plot(X, F1)
# plt.plot(X, F2)
# plt.plot(X, F3)

# plt.show()

# ------------------------------------------------

X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)

F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)

startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3.1, 3.1
# plt.axis([startx, endx, starty, endy])

#plt.plot(X, F1)
#plt.plot(X, F2)
#plt.plot(X, F3)
#plt.plot(X, F1, 'ro')
#plt.plot(X, F2, 'bx')

# plt.show()

# ------------------------------------------------

X = np.linspace(0, 2 * np.pi, 50, endpoint=True)

F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
F4 = np.cos(X)

# plt.plot(X, F1, color="blue", linewidth=2.5, linestyle="-")
# plt.plot(X, F2, color="red", linewidth=1.5, linestyle="--")
# plt.plot(X, F3, color="green", linewidth=2, linestyle=":")
# plt.plot(X, F4, color="grey", linewidth=2, linestyle="-.")

# plt.show()


# ------------------------------------------------

"""


Die allgemeine Syntax von fill_between:
    
    fill_between(x, y1, y2=0, where=None, interpolate=False, **kwargs)

Parameter 	Bedeutung
--------------------------------
x 	            Ein Array mit N Elementen mit X-Werten
y1 	            Ein Array mit N Elementen (oder ein Skalar) von Y-Daten
y2 	            Ein Array mit N Elementen (oder ein Skalar) von Y-Daten
where 	        Wenn auf None gesetzt, wird per Default alles gefüllt. Wenn es nicht auf None gesetzt wird, so wird 
                ein numpy boolean-Array erwartet mit N Elementen. Es werden nur dann die Regionen eingefärbt, bei denen 
                where==True ist.
interpolate 	Wenn True, so wird zwischen zwei Linien interpoliert, um den genauen Schnittpunkt 
                zu finden. Andernfalls werden die Start- und Endwerte nur als explizite Werte auf der Region erscheinen.
kwargs 	        Schlüsselwort-Argumente, die an PolyCollection übergeben werden.
"""

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Y = np.sin(2*X)

plt.plot(X, Y, color='blue', alpha=1.00)

plt.fill_between(X, 0, Y, color='blue', alpha=.1)
plt.show()
