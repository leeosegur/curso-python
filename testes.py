#!python3.12.1

"""
#Primeiro Code:

for num in range(1,201):
    if num % 2 != 0:
        continue
    print(num)
"""
##################################################
"""
#Segundo Code
import sys

infos = {
    "Temperatura": None,
    "Umidade" : None
}

#keys = infos.keys()

for key in infos.keys():
    try:
        infos[key] = float(input(f'Qual a {key}?').strip())
    except ValueError:
        log.error(f'{key.capitalize()} inválida')
        sys.exit(1)

print(infos["Temperatura"])
print(infos["Umidade"])
"""
##################################################