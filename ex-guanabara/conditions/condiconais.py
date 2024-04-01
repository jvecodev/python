from random import randint
import time
computador = randint(0,5)
print('=-='* 10) 
jogador = int(input('Tente acertar um número de 0 e 5!!'))
print ('Processando... ')
time.sleep(3)
if jogador == computador:
    print('Parabéns, você ganhou')
else:
    print('Que pena, não foi dessa vez')

print('=-='* 10)  

#velocidade acima do limite

velocidade = int(input('Qual é a sua velocidade: '))

if velocidade < 60:
    print ('Muito bem, dirija com segurança!')
    
else:
    print ('Limite de velocidade ultrapassado, pague uma multa R$ 100 mais o excesso') 
    excesso = (velocidade - 60)*7   
    print('Deverá pagar um valor de R${:.2f}, 7 reais por cada km ultrapassado.'.format(excesso))

#Par ou ímpar 
numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é par'.format(numero))

else:
    print('O número {} é ímpar'.format(numero))
    
    