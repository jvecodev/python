# No caso de estruturas de respeticao, utilizo o list comprehension para simplificar o codigo, com for ou while 
import os 

os.system('cls')

lista = [

    numero * 2
    for numero in range(1,10)
]

print(lista)


# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 50},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 20},
    {'nome': 'p4', 'preco': 70},
    {'nome': 'p5', 'preco': 90},
    {'nome': 'p6', 'preco': 10},
    {'nome': 'p7', 'preco': 100},
    {'nome': 'p8', 'preco': 80},
    {'nome': 'p9', 'preco': 40},
    {'nome': 'p10', 'preco': 60},
]
def valores(produto):
    if produto['preco'] >= 50:
        print()
        print('Produtos caros: ', produto['nome'])
        print()
    return produto['nome']

novo_produto = [
    valores(produto)
    for produto in produtos
]

print(*novo_produto, sep=' - ')

