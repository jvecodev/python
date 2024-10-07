# No caso de estruturas de respeticao, utilizo o list comprehension para simplificar o codigo, com for ou while 
import os 

os.system('cls')

# lista = [

#     numero * 2
#     for numero in range(1,10)
# ]

# print(lista)


# # Mapeamento de dados em list comprehension

# produtos = [
#     {'nome': 'p1', 'preco': 50},
#     {'nome': 'p2', 'preco': 30},
#     {'nome': 'p3', 'preco': 20},
#     {'nome': 'p4', 'preco': 70},
#     {'nome': 'p5', 'preco': 90},
#     {'nome': 'p6', 'preco': 10},
#     {'nome': 'p7', 'preco': 100},
#     {'nome': 'p8', 'preco': 80},
#     {'nome': 'p9', 'preco': 40},
#     {'nome': 'p10', 'preco': 60},
# ]
# def valores(produto):
#     if produto['preco'] >= 50:
        
#         return produto['nome']
    
#     else:
#         return 'Produto barato'

# novo_produto = [
#     valores(produto)
#     for produto in produtos
# ]

# print('Produtos caros',*novo_produto, sep=' - ')

def valores(x, y, z, n):
    if x + y + z <= n:
        return (x, y, z)
    
    else:
        return 'Soma maior que n'
    
valorx = int(input('Digite o valor de x: '))
valory = int(input('Digite o valor de y: '))
valorz = int(input('Digite o valor de z: '))
valorn = int(input('Digite o valor de n: '))

menores_n = [
    valores(x, y, z, valorn)
    for x in range(valorx + 1)
    for y in range(valory + 1)
    for z in range(valorz + 1)
]

print('Lista de valores que somados são menores ou iguais a n:', *menores_n, sep=' - ')


