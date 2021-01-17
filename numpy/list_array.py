import numpy as np
# Um den Speicherverbrauch einer Liste zu berechnen, werden wir die Funktion
# "getsizeof" aus dem Modul "sys" benutzen.
from sys import getsizeof as size
import time

lst = [24, 12, 57]

size_of_list_object = size(lst)   # nur die Liste, ohne Elemente
size_of_elements = len(lst) * size(lst[0])  # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements

print("Größe ohne Größe der Elemente: ", size_of_list_object)
print("Größe aller Elemente: ", size_of_elements)
print("Gesamtgröße der Liste: ", total_list_size)

print("**********************************************")

lst = [24, 12, 57, 42]
size_of_list_object = size(lst)
size_of_elements = len(lst) * size(lst[0])  # 24, 12, 57, 42
total_list_size = size_of_list_object + size_of_elements

print("Größe ohne Größe der Elemente: ", size_of_list_object)
print("Größe aller Elemente: ", size_of_elements)
print("Gesamtgröße der Liste: ", total_list_size)

print("**********************************************")

lst = []
print("Speicherbedarf einer leeren Liste: ", size(lst))

print("**********************************************")

a = np.array([24, 12, 57])
print(size(a))

e = np.array([])
print(size(e))

print("**********************************************")

a = np.array([24, 12, 57], np.int8)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int16)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int32)
print(size(a) - 96)
a = np.array([24, 12, 57], np.int64)
print(size(a) - 96)
