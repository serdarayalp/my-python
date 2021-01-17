import numpy as np

"""
Maschinengenauigkeit
--------------------

Die Maschinengenauigkeit "eps (ε)" ist die kleinste positive Zahl, für die auf dem Computer gilt:

    1 + eps != 1 (oder 1 + eps > 1)

Für positive Zahlen, die kleiner als eps (ε) sind, gilt somit:

    1 + eps = 1

"1 + eps" wird also nach der Addition wieder auf 1 gerundet. 

-----------------------------------------------

Absoluter Fehler:
    Der absolute Fehler ist der Unterschied zwischen gemessenem Ist-Wert der Messgröße x und dem wahren Wert 
    der Messgröße xw. 

        absoluter Fehler = x - xw

Relativer Fehler:

        relativer Fehler = absoluter Fehler / x

-----------------------------------------------

Auslöschung:
Unter Auslöschung versteht man den Verlust an Genauigkeit bei der Subtraktion fast gleich großer Gleitkommazahlen.


Subtrahiert man zwei p-stellige, fast gleich große Zahlen, die in den ersten k Stellen übereinstimmen, 
so gehen im Ergebnis von den möglichen p Stellen k verloren. Es sind also nur noch p-k  Stellen ungleich Null. 
Die Information, dass die ersten k Stellen sich zu Null aufgehoben haben, geht dabei verloren. Die Genauigkeit 
des Ergebnisses vermindert sich um diese k Stellen.

Unterscheiden sich die Zahlen in den letzten p-k Stellen lediglich um Rundungsfehler, dann hat das Ergebnis keine 
Aussagekraft. Es sollte als solches nicht in weitere Berechnungen einfließen. 
"""


def macheps():
    """
        Wikipedia: 
         * Die Maschinengenauigkeit gibt den maximalen relativen Rundungsfehler an. 
         * In der Praxis wird die Maschinengenauigkeit als kleinste positive Gleitkommazahl ε 
            ermittelt, für die auf der betreffenden Maschine die Bedingung 1 + ε > 1 erfüllt ist.
        """

    format = np.dtype('float64')  # 2.220446049250313e-16

    eps = format.type(1.0)
    one = format.type(1.0)
    two = format.type(2.0)

    epsilon_counter = one

    while (one + epsilon_counter) != one:
        eps = epsilon_counter
        epsilon_counter = epsilon_counter / two

    return eps


print(1 + macheps())

print(macheps())
