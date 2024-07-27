from produtos_modulos import produtos
import copy
import os
# Limpando o terminal com cls por ser  windows 11

os.system('cls')


novos_produtos = copy.deepcopy(produtos)

for indice in novos_produtos:
    indice['preco'] = indice['preco'] * (10/100) + indice['preco']

def aumentarpreco():
    for indice in novos_produtos:
        print(f'\nProduto: {indice['nome']} - Preço: {indice['preco']}\n')

aumentarpreco()

print('=-'*30)

def ordenarprodutos():
    novos_produtos.sort(key=lambda x: x['nome'])
    for indice in novos_produtos:
        print(f'\nProduto: {indice['nome']} - Preço: {indice['preco']}\n')
ordenarprodutos()

print('=-'*30)

def ordenarpreco():
    novos_produtos.sort(key=lambda x: x['preco'])
    for indice in novos_produtos:
        print(f'\nProduto: {indice['nome']} - Preço: {indice['preco']}\n')
ordenarpreco()

