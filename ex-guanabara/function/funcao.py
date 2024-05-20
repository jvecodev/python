#funcao
# def area(largura, comprimento):
#     a = largura * comprimento
#     print(f'A área de um terreno {largura}x{comprimento} é de {a}m²')
# l = float(input('Largura(m):'))
# c = float(input('Comprimento(m): '))
# area(l, c)

#Escreva
# def escreva(msg):
#     tam = len(msg) 
#     print('~'*tam)
#     print(msg)
#     print('~'*tam)
# frase = str(input('Digite uma frase: '))
# escreva(frase)
# while True:
#     resp = str(input('Quer continuar? [S/N]')).upper()
#     if resp == 'N':
#         break
#     else:
#         frase = str(input('Digite uma frase: '))
#         escreva(frase)
# escreva('Fim do programa')  
# from time import sleep      
# inicio = int(input('Digite um número de entrada: '))
# fim = int(input('Digite um número de saída: '))
# passo = int(input('Digite o passo: '))
# for c in range(inicio, fim+1, passo):
    
#     print(f'{c} →', end=' ',flush = True)#→Esta nova funcao existe par alternar os intervalos de tempo, funcionando um sleep após cada número.
#     sleep(0.5)
# print('{Fim}')

# def maior (*num):
#     print('Analisando os valores... ')
#     contador = maior = 0
#     while True:
#         contador += 1
#         n = int(input(f'Digite {contador}° número: '))
        
#         if contador == 1:
#             maior = n
#         else:
#             if n > maior:
#                 maior = n
#         resp = str(input('Quer continuar? [S/N]')).upper()
#         if resp == 'N':
#             break
#     print(f'Você digitou {contador} números e o maior valor foi {maior}')
# maior()

from time import sleep
from random import randint

def sorteia(lista):      
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)  
        lista.append(n)   
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
        
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2==0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
# help(input) > #help é uma função que mostra a documentação de uma função

    
    


            

 

