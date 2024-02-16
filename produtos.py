#!python3.12.1
"""
Cadastro de Produtos.
"""

__version__ = "0.0.1"

#import pprint
from pprint import pprint

produto = {
    "nome" : "Caneta",
    "cores" : ["azul","branco"],
    "preco" : 3.23,
    "dimens]ao" : {
        "altura" : 12.1,
        "largura" : 0.8,
    },
    "em_estoque" : True,
    "codigo" : 45678,
    "codebar" : None,
}

cliente = {
    "nome" : "Leonardo Segur"
}

compra = {
    "cliente" : cliente,
    "produto" : produto,
    "quantidade" : 3
}

totalCompra = compra['quantidade'] * compra['produto']['preco']
cor = list(produto['cores'])

print(f"O cliente {compra['cliente']['nome']} " 
        f"comprou {compra['quantidade']} unidades de caneta "
        f"e pagou o total de {totalCompra}")