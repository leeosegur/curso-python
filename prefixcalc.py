#!python3.12.1
"""
Calculadora Prefix

Funcionamento:

[OPERAÇÃO] [N1] [N2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 5
9
"""

__version__ = "0.0.1"

import sys
arguments = sys.argv[1:]

if not arguments:
    operation = input("Operação:")
    n1 = input("N1:")
    n2 = input("N2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print(f"Numero de Argumentos invalidos, os argumentos declarados foram {arguments}")
    print("ex: `sum 5 5")
    sys.exit("Error:1")
