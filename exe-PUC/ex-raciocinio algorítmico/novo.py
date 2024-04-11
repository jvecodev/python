#aluno irresponsável
contador = 0
print ('Escreva em seu caderno')
while contador < 11:
    print('Eu amo Racícinio Algorítmico')
    contador +=1
print ('Você acha que me engana. Não use laços')    

# numero secreto from random import randint
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
  

        

