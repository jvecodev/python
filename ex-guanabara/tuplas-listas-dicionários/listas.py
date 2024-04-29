#exercicios 
# lista = []
# contador = 0
# for count in range(5):
#     lista.append (int(input(f'Digite um valor para posição {count}: ')))
#     if count == 0:
#         maior = lista[count]
#         menor  = lista[count]
#     else:
#         if lista[count] > maior:
#             maior = lista[count]
#         elif lista[count] < menor:
#          lista[count] = menor 
# print('-'*15)
# lista.sort()
# print(f'Você digitou os números {lista}')
# print(f'{menor} = menor valor, nas posiçõe/s ', end='')
# for i, v in enumerate(lista):
#    if v == menor:
#       print (f'{i}...', end= '')

# print(f'{maior} = maior valor, ', end='')
# for i, v in enumerate(lista):
#    if v == maior:
#       print (f'{i}...' )

#outro exercício listas

# numero = list()
# contador = 0
# while True:
#    contador += 1
#    num = int(input(f'Digite o {contador} valor:'))
#    if num  not in numero:
#       numero.append(num)
#       print('Valor digitado com sucesso!')
#    else:
#       print('Número já digitado!')
#    opcao = str(input('Quer continuar? [S/N]').upper().strip())
#    if opcao != 'N' and opcao != 'S':
#       print('Apenas valores permitidos!')
#    elif  opcao in 'N':
#       break
# print('====================')
# numero.sort()
# print(f'Você digitou os valores {numero}')

#usando insert

# lista = []
# for count in range(0, 5):
#     numero = int(input(f'Digite o  valor: '))
#     if count == 0 or numero > lista[-1]:
#         lista.append(numero) 
#         print('Adicionado ao final da lista!')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if numero <= lista[pos]:
#                 lista.insert(pos, numero)
#                 print(f'Adicionado na posição {pos} da lista')
#                 break
#             pos+=1

# print('===================')

# print(f'Os valores digitados em ordem são {lista}')           

# Sort Reverse
# lista = []
# contador = 0
# while True:
#    contador += 1
#    numero = int(input(f'Digite {contador} valor: '))
#    lista.append(numero)
#    opcao = str(input('Deseja prosseguir? [S/N]').upper())
#    if opcao in 'N':
#       break
# lista.sort(reverse=True)
# print(f'Numero digitados: {lista}')   
# if 5 in lista:
#    print('O valor 5 faz parte da lista!')
# else:
#    print('O valor 5 não faz parte da lista!')

#lista 
lista = list()
pares = list()
impares = list()
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    opcao = str(input('Quer continuar? [S/N]: ').upper())
    if opcao in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
lista.sort()
print(f'Valores digitados {lista}') 
pares.sort()
print(f'Valores pares digitados {pares}')
impares.sort()
print(f'Valores ímpares digitados {impares}')

#regulamento de expressao
expressao = str(input('Digite uma expressão: '))
pilha = []
for valor in expressao:
    if valor == '(':
        pilha.append('(')
    elif valor == ')':
        if len(pilha) > 0:
            pilha.pop()    
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Expressão invalida!')




            