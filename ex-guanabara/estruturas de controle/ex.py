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

import random
computador = (random.randint(1,100))
contador = 0

numero = 0
print('='*10)
print ('Desafio')
print ('='*9)
while numero != computador:
    numero = int(input('Tente adivinhar o numero de 1 a 100: '))
    if numero < computador:
        print ('Diga um número maior')
        print('Tente novamente')
        
    elif numero > computador:
        print ('Diga um número menor')
        print('Tente novamente')

    else:
        print('Parabéns')
    contador += 1
print('Você acertou na {} tentativa'.format(contador))









          