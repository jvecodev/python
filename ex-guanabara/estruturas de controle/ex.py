# pergunta2 = 'S'
# pergunta3 = 0
# while pergunta2 == 'S':
#     valor = int(input('Digite um valor: '))
#     pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
#     if pergunta2 != 'S' and pergunta2 != 'N':
#         pergunta3 = str(input('Não compreendo, digite novamente:'))
#         pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
       
# print('Fim')

#numero secreto

# import random
# computador = (random.randint(1,100))
# contador = 0

# numero = 0
# print('='*10)
# print ('Desafio')
# print ('='*9)
# while numero != computador:
#     numero = int(input('Tente adivinhar o numero de 1 a 100: '))
#     if numero < computador:
#         print ('Diga um número maior')
#         print('Tente novamente')
        
#     elif numero > computador:
#         print ('Diga um número menor')
#         print('Tente novamente')

#     else:
#         print('Parabéns')
#     contador += 1
# print('Você acertou na {} tentativa'.format(contador))

#MENU 
# from time import sleep 
# valor1 = float(input('Digite o primeiro valor: '))
# valor2 = float (input('Digite o segundo valor: '))
# opcao = 0
# print ('='*9)
# while opcao != 5:
#     print ('''Ecolha: 
#            [1] somar
#            [2] multiplicar
#            [3] maior
#            [4] novos números
#            [5] sair do programa ''')
#     opcao = int(input('Opção: '))
#     if opcao ==1:
#         print(valor1 + valor2)
#         sleep(.5)
#     elif opcao ==2:
#         print (valor1 * valor2)
#         sleep(.5)
#     elif opcao ==3:
#         if valor1 > valor2:
#            maior = valor1
#            print ('O número {} é maior que o número {}. '.format(valor1, valor2)) 
#            sleep(.5)

#         elif valor1 == valor2:
#             maior = print('O numero {} e {} são identicos identicos.'.format(valor1, valor2))
#             sleep(.5)
#         else:
#             maior = valor2
#             print ('O número {} é maior que o número {}. '.format(valor2, valor1))
#             sleep(.5) 
#     elif opcao == 4:
#         valor1 = float(input('Digite o primeiro valor: '))
#         valor2 = float (input('Digite o segundo valor: '))
#     elif opcao == 5:
#         print('Finalizando ')
#         sleep(2)
#     else:
#         print('Número não identificado')
#         print ('Tente novamente')
#         sleep(.5)
#         valor1 = float(input('Digite o primeiro valor: '))
#         valor2 = float (input('Digite o segundo valor: '))
# print ('Tente sempre que desejar!!')
# print ('='*9)

# #PA
# print ('== Resolvendo uma PA ==')

# numero = int(input('Digite um número para calcularmos uma Progressão: '))
# razao = int(input('Qual será a razão? '))
# termo = numero
# contador = 1
# while contador <= 10:
#     print ('{} →'.format(termo), end=" ")
#     termo += razao
#     contador +=1
# print ('FIM')

#super PA
# print ('\n== Resolvendo uma  Super PA ==')

# numero = int(input('Digite um número para calcularmos uma Progressão: '))
# razao = int(input('Qual será a razão? '))
# termo = numero
# contador = 1
# total = 0
# mais = 10
# while mais != 0:
#     total += mais 
#     while contador <= total:
#         print ('{} →'.format(termo), end=" ")
#         termo += razao
#         contador +=1
#     print('PAUSA')
#     mais = int(input('Deseja prosseguir com quantos termos: '))
# print ('Progressão realizada com {} termos.'.format(total))

#sequencia de Fibonacci
# print ('='*9)
# print('Sequência Fibonacci')
# print ('='*9)
# numero = int(input('Quantos termos deseja? '))
# termo1 = 0
# termo2 = 1


# print ('~'*9)
# print('{} → {}'.format(termo1, termo2), end =' ')
# contador = 3
# while contador <= numero:
#         termo3 = termo1 + termo2
#         print ('→ {}'.format(termo3), end=' ')
#         termo1 = termo2
#         termo2 = termo3
#         contador +=1 
# print ('FIM')
# print ('~'*9)

# parada = 0
# contador = 0
# soma = 0
# parada = int(input('Digite [999] para parar a soma: '))
# while parada != 999:
#     soma = soma + parada 
#     contador += 1
#     parada = int(input('Digite [999] para parar a soma: '))
# print('Você digitou {} numero, cujo a soma é = {}'.format( contador, soma)) 

# Para a soma ser executada corretamente, coloca a variável fora do while e o final do while!!!


print ('\nExercício 65')
print('~'*10)
numero2 = 'S'
media = soma = contador = maior = menor = 0
while numero2 in 'S':
    numero1 = int(input('Digite um numero: '))
    soma += numero1
    contador += 1 
    if contador == 1:
         maior = menor = numero1
    else:
        if numero1 > maior:
            maior = numero1
        if numero1 < menor:
            menor = numero1
    numero2 = str (input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / contador 
print ('\nVoce digitou {} numero, com a media = {}'.format(contador, media ))
print ('\n O maior número foi {} e o menor foi {}'.format (maior, menor))
print('~'*10)




   






















          