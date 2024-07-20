# kwargs = keyword arguments = Argumentos nomeados
# Juntamente utilizados com dicionarios para passar argumentos nomeados

import os
# Limpando o terminal com cls por ser  windows 11

os.system('cls')
print('='*50)

def mostrarArgumentos(**kwargs):
    print(kwargs)

mostrarArgumentos(nome="Lucas", sobrenome="Santos", idade=20)  # → Mostrará o um dicionario com os argumentos passados

# Para expressar sem formato de dicionario 
print('='*50)


def mostrarArgumentos2(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')

mostrarArgumentos2(nome="Lucas", sobrenome="Santos", idade=20)  # → Mostrará o um dicionario com os argumentos passados

# Qualquer argumetno nao nomeado entrará em args 
print('='*50)


def mostrarArgumentos3(*args, **kwargs):
    print(args, '→ não nomeados ')
    print(kwargs, '→ nomeados'	)

mostrarArgumentos3(1, 2, 3, nome="Lucas", sobrenome="Santos", idade=20)  # → 1,2,3 não nomeados e nome, sobrenome, idade são nomeados


#exemplo passando um dicionario para a função

print('='*50)

configuracao = {
    'nome': 'Lucas',
    'sobrenome': 'Santos',
    'idade': 20
}
#                  Representa um kwargs
mostrarArgumentos(**configuracao)  # → Mostrará o um dicionario com os argumentos passados