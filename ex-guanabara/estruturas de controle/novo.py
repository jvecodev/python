
from random import randint
computador = randint(0,100)
contador = 0
print('==== Desafio ====')
while True:
    pergunta = int(input('\nAcerte um numero de 0 a 100: '))
    if pergunta > computador:
        print('\nDiga um número menor ')
        print('\nTente novamente ')
        contador =+1
    if pergunta < computador:
        print ('\nDiga um número maior ') 
        print ('\nTenta novamente ')
        contador =+1
    else:
        print ('\nParabéns pelo acerto!!!')
print ('\nAcertou o resultado em {} tentativas'.format(contador))     
print ('Fim ')   