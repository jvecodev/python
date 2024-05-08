# galera = list()
# dados = list()
# contador = 0
# menor = maior = 0
# while True:
#     contador += 1
#     dados.append(str(input('Digite seu nome: ')))
#     dados.append(float(input('Digite seu peso: ')))
    
#     if len(galera) == 0:
#         menor = maior = dados[1]
#     else:
#         if dados[1] > maior:
#             maior = dados[1]
#         elif dados[1] < menor:
#             menor = dados[1]

#     galera.append( dados[:])
#     dados. clear()
#     print('='*20)
#     opcao = str(input('Deseja prosseguir? [S/N]').upper())
#     print('='*20)
#     if opcao in 'N':
#         break
# print('='*20)
# print(f'{contador} perfis foram registradas')
# print(f'Os dados foram {galera}')
# print(f'O maior peso foi {maior} kg respectivamente do ',end='')
# for p in galera:
#     if p[1] == maior:
#         print(f'{p[0]}')
# print(f'O menor peso foi {menor} kg respectivamente do ',end='')
# for p in galera:
#     if p[1] == menor:
#         print(f'{p[0]}')

#pares e impares

numeros = [[], []]

for count in range (7):
    dados = int(input(f'Digite o {count} valor: '))
    if dados % 2 == 0:
        numeros [0].append(dados)
    else:
        numeros [1].append(dados)
numeros[0].sort()
print(f'Os valores pares são {numeros[0]}')
numeros[1].sort()
print(f'Os valores ímpares são {numeros[1]}')

#matrizes 
# print('='*30)
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# soma = maior = 0

# for l in range (0,3):
#     for c in range (0,3):
#         matriz[l] [c]= float(input(f'Digite um valor para {l}, {c}:  '))
# print('='*30)
# for l in range(0,3):
#     for c in range (0,3):
#         print(f'[{matriz [l][c]:^5}]',end=' ')
#         if matriz[l] [c] %2 ==0:
#             soma += matriz [l] [c]
#         if l == 0 and c == 0:
#             matriz[l] [c] = maior
#         if matriz [l] [c] > maior:
#             maior = matriz [l] [c]
            
            
#     print()
# print('A soma dos valores pares é igual a: ',soma)
# print('O maior valor digitado é: ', maior )
# print('#'*20)

#sorteio mega sena
from random import randint
from time import sleep

lista = list()
jogos = list()

quantidade = int(input('Quantos jogos deseja? '))
tot = 1

while quantidade >= tot:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador > 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    tot += 1
print(f'Sorteando {quantidade} jogos')
for i, l in enumerate(jogos):
    print(f'jogo{i+1}: {l}')
    sleep(1)
print('')
        






        
        
    



