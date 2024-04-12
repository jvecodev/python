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
from time import sleep 
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float (input('Digite o segundo valor: '))
opcao = 0
print ('='*9)
while opcao != 5:
    print ('''Ecolha: 
           [1] somar
           [2] multiplicar
           [3] maior
           [4] novos números
           [5] sair do programa ''')
    opcao = int(input('Opção: '))
    if opcao ==1:
        print(valor1 + valor2)
        sleep(.5)
    elif opcao ==2:
        print (valor1 * valor2)
        sleep(.5)
    elif opcao ==3:
        if valor1 > valor2:
           maior = valor1
           print ('O número {} é maior que o número {}. '.format(valor1, valor2)) 
           sleep(.5)

        elif valor1 == valor2:
            maior = print('O numero {} e {} são identicos identicos.'.format(valor1, valor2))
            sleep(.5)
        else:
            maior = valor2
            print ('O número {} é maior que o número {}. '.format(valor2, valor1))
            sleep(.5) 
    elif opcao == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float (input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando ')
        sleep(2)
    else:
        print('Número não identificado')
        print ('Tente novamente')
        sleep(.5)
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float (input('Digite o segundo valor: '))
print ('Tente sempre que desejar!!')
print ('='*9)

















          