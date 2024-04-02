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

if velocidade <= 60:
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

#outro desafio/dependera do cliente
    
'''distancia = float(input('Digite a distancia que você irá percorrer: '))
print ('Está preste a percorrer uma distancia de {:.2f} km!'.format(distancia))

#se a viagem for acima dos 200km, haverá um desconto de 5 centavos 


if distancia <= 200:
    preço = distancia * 0.50
else:
    distancia > 200 
    preço =  distancia*0.45
print ('Valor final = {:.2f}'.format(preço))'''

#if simplificado

distancia = float(input('Digite a distancia que você irá percorrer: '))
print ('Está preste a percorrer uma distancia de {:.0f} km!'.format(distancia))
preço = distancia*0.50 if distancia < 200 else distancia *0.45 
print('O valor final a pagar será de {:.2f}'.format(preço))

# ano bissexto 

ano = int(input('Qual ano deseja analisar? '))

if ano % 4==0 and ano % 100!=0 or ano %400 == 0:
    print('O ano {} É bissexto'.format(ano))

else:
    print ('O ano {} NÃO é bissexto'.format(ano)) 

# menor e maior
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite o segundo: ')) 
numero3 = int(input('Digite o terceiro: ')) 
#identificando o menor 
menor = numero2
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero3 < numero2 and numero3 < numero1:
    menor = numero3
#identificando o maior
maior = numero2
if numero1 > numero2 and numero1 > numero3:
    maior = numero1

if numero3 > numero2 and numero3 > numero1:
    maior = numero3
print('O menor numero é: {} '.format(menor))    
print ('O maior numero é: {}'.format(maior))

#ultimo
print ('---DESAFIO TRIÂNGULO---')

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print('Os valores {}, {}, {} formam um triângulo'.format(lado1, lado2, lado3))
else:
    print('Não será possível formam um triângulo')

    









    
    