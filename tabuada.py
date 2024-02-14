#!python3.12.1
"""
IMPRIME A TUBUADA DO 1 AO 10.

USAGE:

------TABUADA DO 1

1 x 1 = 1
2 x 1 = 2 
3 x 1 = 3
.............
#####################
------TABUADA DO 2

1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
.............
#####################
"""
__version__ = "0.0.2"
__author__ = "Leonardo Segur"
__license__ = "Unlicense"

#templete = """
#---Tabuada do 2---

#    {bloco}
#"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
#for n1 in numeros:
    #bloco = ""
    #for n2 in numeros:
        #operacao = f"{n1} x {n2} = {n1 * n2}"
        #bloco  + bloco + bloco
        #print(operacao)
        #print(templete.format(bloco=bloco))
######################################################################

numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^21}".format(f"Tabuada do {n1}" + "\U0001FAE0"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)