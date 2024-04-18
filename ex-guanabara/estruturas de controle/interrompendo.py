# # Primeiro exercício com break
# print ('=-'*10)
# print('[999] Trata-se da flag de parada ')
# numero = 0
# contador = soma = 0
# while True:
#     numero = int(input('\nDigite um número: '))
#     if numero == 999:
#         # Este termo jogará a proxima ação para fora do laço!
#         break 

#     contador +=1
#     soma += numero
# print (f'foram digitados {contador} numeros, cuja a soma é {soma}.')

# print('=-'*20)
# # Tabuada aleatória
# print('\nFlag de parada → Valor negativo')

# opcao = 'S'
# while opcao == 'S':
    
#     numero = int(input('Digite outro numero para vermos a tabuada: '))
#     if numero < 0:
#         break
#     for n in range (1,11):
#         print (f'{numero}x{n} = {n*numero}')
#     print('=-'*20)
#     opcao = str(input('Quer continuar? [S/N] ').strip().upper())

# print ('Programa encerrado')    

#par ou impar
# from random import randint
# contador = 0
# print ('\n===== PAR/IMPAR =====')
# while True:
#     jogador = int(input('\nDigite um numero: '))
#     computador = randint(0,10)
#     total = jogador + computador
#     opcao = ' '
#     while opcao not in 'PI':
#         opcao = str(input('Par ou Ímpar, [P/I]?').strip().upper()[0])
#         print (f'Sua opção foi {jogador} e opção adversário foi {computador}!')
#         print ('Com uma soma de: ', total)
#     if opcao == 'P':
#         if total %2 == 0:
#             print ('PARABÉNS PELA VITÓRIA!')
#             print ('\nDEU PAR')
#             contador += 1
#         else:
#             print('VOCÊ PERDEU!',end=' ')
#             print ('Deu ímpar')
#             print('\nNenhum problema, tente novamente!')
#             break 
#     elif opcao == 'I':
#         if total %2 != 0:
#             print('PARABÉNS PELA VITÓRIA!')
#             print('\nDEU ÍMPAR')
#         else:
#             print('VOCÊ PERDEU!',end=' ')
#             print ('Deu par!')
#             print('\nNenhum problema, tente novamente!')
#             break 
#         print ('\nVamos jogar novamente!')
# print (f'\nGAME OVER. Você foi vencedor {contador} vezes')        

#cadastro
print('-'*20)
print('CADASTRE UMA PESSOA')
contador18 = contadorH = contadorm = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        contador18 += 1
    sexo = str(input('DIgite sua sexualidade  [M/F]:') .strip().upper())
    if sexo == 'M':
        contadorH += 1
    if sexo == 'F' and idade < 20:
        contadorm += 1
    print('-'*20)
    opcao = str(input('Quer continuar [S/N]').strip().upper())
    if opcao == 'N':
        break 
    print('-'*20)
print(f'Temos um total de {contador18} acima dos 18 anos')    
print(f'Ao todo temos {contadorH} homem cadastrados')
print(f'E temos {contadorm} mulheres com menos de 20 anos ')
print ('Obrigado volte sempre!')  


# mercadao
print('\n--------------------')
print('SUPER MERCADÃO')
print('-'*20)
soma = contador = contadorP = 0

while True:
    produto = str(input('Produto: '))
    contadorP += 1
    preco = float(input('Preço: '))
    print('-'*20)
    opcao = str(input('Novo Produto? [S/N]').strip().upper())
    soma += preco
    if preco > 1000:
        contador += 1
    if  contadorP == 1:
        maior = produto
        menor = produto
    else:
        if produto > maior:
            maior = produto
        if produto < menor:
           menor = produto
    if opcao == "N":
        break
    
    print ('-'*20)
print (f'Total da Compra: R${soma:.2f}')
print (f'Temos {contador} produtos/produto acima de R$1000,00 ')    
print (f'Produto mais caro <{maior}>. Produto mais barato <{menor}>')
print ('Obrigado, volte sempre!!')






      
    

    
    








                    
                            

        



        


   


