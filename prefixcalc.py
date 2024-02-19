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
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operação invalida")
    print(valid_operations)
    sys.exit(1)

valid_numbers = []

for num in nums:
    if not num.replace(".", " ").isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
        valid_numbers.append(num)

n1, n2 = valid_numbers


# TODO : Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")