#!python3.12.1

"""
Objetivo deste programa é gerar um relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.

"""

__version__ = "0.0.1"
import os
import sys

#LBYL - LOOK BEFORE YOU LEAP

#if os.path.exists("names.txt"):
#    print("The file exist:")
#    input("...")    # RACE CONDITION
#    names = open("names.txt").readlines()
#else:
#    print("[ERROR:]File names.txt not found.")
#    sys.exit(1)

#if len(names) >= 1:
#    print(names[1])
#else:
#    print("[ERROR:]Missing name in the list")
#    sys.exit(1)

###
# EAFP - EASY TO ASK FORGIVENESS THAN PERMISSION
###

try:
    names = open("names.txt").readlines()
except FileNotFoundError: # Bare except
    print("[ERROR:]File names.txt not found.")
    sys.exit(1)
except AttributeError:
    print("[ERROR:]AttributeError in file.")
    sys.exit(1)
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

#except (FileNotFoundError, AttributeError) as e:
#   print(f"{str(e)}.")
#   sys.exit(1)

try:
    print(names[1])
except:
    print("[ERROR:]Missing name in the list")
    sys.exit(1)