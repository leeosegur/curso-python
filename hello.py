#!python3.12.1
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Usage:

Tenha a variavel langue devidamente configurada ex:

    export LANG=pt_br

Execução:

    python hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Leonardo Segur"
__license__ = "Unlicense"
#Dunder = __ (2 Underlines)

import os
import sys


arguments = {}

for arg in sys.argv[1:]:
    print(f"{argv=}")

#current_language = os.getenv("LANG", "it_IT")[:5]
current_language = "it_IT"

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá ,Mundo!",
    "it_IT": "Ciao, Monde!"
}


#if current_language == "pt_BR":
#    msg = "Olá, Mundo!"
#elif current_language == "it_IT":
#    msg = "Ciao, Mondo!"

print(msg[current_language])