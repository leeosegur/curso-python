#!python3.12.1
"""
IMPRIME A TUBUADA DO 1 AO 10.

USAGE:

TABUADA DO 1
1
2
3
.............
TABUADA DO 2
2
4
6

"""
__version__ = "0.0.1"
__author__ = "Leonardo Segur"
__license__ = "Unlicense"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print(">>>>>>>>>>>>>><<<<<<<<<<<<<<")