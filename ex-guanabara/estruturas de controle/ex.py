pergunta2 = 'S'
pergunta3 = 0
while pergunta2 == 'S':
    valor = int(input('Digite um valor: '))
    pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
    if pergunta2 != 'S' and pergunta2 != 'N':
        pergunta3 = str(input('Não compreendo, digite novamente:'))
        pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
       
print('Fim')

#numero secreto
import random
computador = (random.randint(1,100))
contador = 0
print('='*10)
while True:
    numero = int(input('Tente adivinhar o numero de 1 a 100: '))
    if numero < computador:
        print ('Diga um número maior')
        print('\nTente novamente')
        contador =+ 1
    elif numero > computador:
        print ('Diga um número menor')
        print('Tente novamente')
        contador =+ 1
    else:
        print('Parabéns!!')
          