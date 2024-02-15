#!python3.12.1
#
"""
Objetivo deste programa é gerar um relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.

"""
#
__version__ = "0.0.1"
__author__ = "Leonardo Segur"
__license__ = "Unlicense"

sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Danca", aula_danca), ("Ingles", aula_ingles), ("Musica", aula_musica)]

# Listar alunos em cada atividade por sala

for nome_atividade, atividades in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    
# Sala1 que tem interseção com a atividade

    atividade_sala1 = set(sala1) & set(atividades)
    atividade_sala2 = set(sala2) & set(atividades)

#    for aluno in atividades:
#        if aluno in sala1:
#            atividade_sala1.append(aluno)
#        elif aluno in sala2:
#            atividade_sala2.append(aluno)

    print(f"A {nome_atividade} sala1:" , (atividade_sala1))
    print(f"A {nome_atividade} sala2:" , (atividade_sala2))
    print("#" * 45)
    print()