pergunta2 = 'S'
pergunta3 = 0
while pergunta2 == 'S':
    valor = int(input('Digite um valor: '))
    pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
    if pergunta2 != 'S' and pergunta2 != 'N':
        pergunta3 = str(input('Não compreendo, digite novamente:'))
        pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
       
print('Fim')

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



    
    

               

               

        
  




 



    