valor1 = int(input('Digite um valor:'))
valor2 = int(input('Digite outro valor:'))
soma = valor1 + valor2
multi = valor1 * valor2
divisao = valor1/valor2
div = valor1//valor2
e = valor1 ** valor2

print ('A soma é {}, o produto é {} e a divisão é {}.'.format(soma, multi, divisao,), end='>>>')
print ('A dvisao inteira é {} e a potência é {}'.format(div, e))

#outro desafio

pergunta = float(input('Quantos reais o senhor tem em sua cateira?'))

cotação = 4.99
multi = pergunta / cotação
print ('Cotação do Dolar em Real:', cotação)
print ('O valor que o senhor arrecadiu foi de:',multi)


