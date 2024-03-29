#exercicio01 proção inteira
""""import math
numero = float(input('Digite um numero de seu interesse: '))
print ('A porção real do seu numero foi {}, já a porção inteira foi {}'.format(numero, math.trunc(numero)))"""

#outro metodo 
#Neste caso pode-se utilizar apenas a função <int>, no entanto apresentara tbm a porção inteira do numero.

from math import trunc
numero01 = float (input('Digite novamente: '))
print ('Porção real {}, porção inteira {}'.format(numero01, trunc(numero01)))

#exe002

''''from math import hypot
oposto = float(input('Digite o valor oposto ao angulo: '))
adjacente = float (input('Digite o valor ao lado ao angulo: '))
hipotenusa = hypot (oposto,adjacente)
print('Com os valores {} de cat.oposto e {} de cat.adjacente, a hipotenusa será aproximadamente {:.2f}.'.format(oposto, adjacente, hipotenusa))'''

import  math 
oposto = float(input('Digite o valor oposto ao angulo: '))
adjacente = float (input('Digite o valor ao lado ao angulo: '))
hipotenusa = math.hypot (oposto,adjacente)
print('Com os valores {} de cat.oposto e {} de cat.adjacente, a hipotenusa será aproximadamente {:.2f}.'.format(oposto, adjacente, hipotenusa))

#exe003

''''from math import cos, sin, tan
angulo = float(input('Digite um ângulo: '))
seno = sin (math.radians(angulo))
cossseno = cos (math.radians(angulo))
tangente =  tan (math.radians(angulo))

print('Portanto o seno é {} = a tangente é {} e o cosseno é {} = '.format(seno, tangente, cossseno))'''

import math 
angulo = float(input('Digite um ângulo: '))
seno = math.sin (math.radians(angulo))
cossseno = math.cos (math.radians(angulo))
tangente =  math.tan (math.radians(angulo))

print('Portanto o seno é {:.2f} = a tangente é {:.2f} e o cosseno é {:.2f} = '.format(seno, tangente, cossseno))

import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
lista = [aluno1,aluno2, aluno3]
escolhido = random.choice(lista)

print('o aluo escolhido foi o', escolhido)












