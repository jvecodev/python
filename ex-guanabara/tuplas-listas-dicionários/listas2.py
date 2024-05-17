# # galera = list()
# # dados = list()
# # contador = 0
# # menor = maior = 0
# # while True:
# #     contador += 1
# #     dados.append(str(input('Digite seu nome: ')))
# #     dados.append(float(input('Digite seu peso: ')))
    
# #     if len(galera) == 0:
# #         menor = maior = dados[1]
# #     else:
# #         if dados[1] > maior:
# #             maior = dados[1]
# #         elif dados[1] < menor:
# #             menor = dados[1]

# #     galera.append( dados[:])
# #     dados. clear()
# #     print('='*20)
# #     opcao = str(input('Deseja prosseguir? [S/N]').upper())
# #     print('='*20)
# #     if opcao in 'N':
# #         break
# # print('='*20)
# # print(f'{contador} perfis foram registradas')
# # print(f'Os dados foram {galera}')
# # print(f'O maior peso foi {maior} kg respectivamente do ',end='')
# # for p in galera:
# #     if p[1] == maior:
# #         print(f'{p[0]}')
# # print(f'O menor peso foi {menor} kg respectivamente do ',end='')
# # for p in galera:
# #     if p[1] == menor:
# #         print(f'{p[0]}')

# #pares e impares

# numeros = [[], []]

# for count in range (7):
#     dados = int(input(f'Digite o {count} valor: '))
#     if dados % 2 == 0:
#         numeros [0].append(dados)
#     else:
#         numeros [1].append(dados)
# numeros[0].sort()
# print(f'Os valores pares são {numeros[0]}')
# numeros[1].sort()
# print(f'Os valores ímpares são {numeros[1]}')

#matrizes 
print('='*30)
soma = 0    
matriz = [[0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0], 
                          ]
for l in range (0,3):
    for c in range (0,5):
        matriz[l] [c]= input(f'Digite um valor para {l}, {c}:  ')

print('='*30)
for l in range(0,3):
    soma = 0
    for c in range(0,5):
        soma += int(matriz[l][c])
        print(f'[{matriz [l][c]:^5}] ',end='→')
    print(f'Soma da linha {l} é {soma}')



print('='*30) 



            
#     print()
# print('A soma dos valores pares é igual a: ',soma)
# print('O maior valor digitado é: ', maior )
# print('#'*20)

# #sorteio mega sena
# from random import randint
# from time import sleep

# lista = list()
# jogos = list()

# quantidade = int(input('Quantos jogos deseja? '))
# tot = 1

# while quantidade >= tot:
#     contador = 0
#     while True:
#         numero = randint(1, 60)
#         if numero not in lista:
#             lista.append(numero)
#             contador += 1
#         if contador > 6:
#             break 
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear
#     tot += 1
# print(f'Sorteando {quantidade} jogos')
# for i, l in enumerate(jogos):
#     print(f'jogo{i+1}: {l}')
#     sleep(1)
# print('')
        

from time import sleep
print ('\n=======Lista compostas=======')
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('DIgite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media] )
    opcao = str(input('Deseja prosseguiir? [S/N]').upper())
    if opcao in 'N':
        break
print('='*20)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('='*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
nova_opcao = str(input('Deseja ver as notas de algum aluno? [S/N]').upper())
if nova_opcao in 'S':
    aluno2 = int(input('Digite o número do aluno: '))
    sleep(0.5)
    print(f'As notas de {ficha[aluno2][0]} são {ficha[aluno2][1]}')
else:
    print('Finalizando o programa. . .')
    sleep(0.5)
print('Muito obrigado por usar o programa !')









        
        
    



