numero =int(input('Digite um valor: '))
print(''' \n Sua opção de conversão: \n
[ 1 ] Base binária
[ 2 ] Base Octal
[ 3 ] Base Hexadecimal \n''')
opcao = int(input('Escolha sua opção:'))
if opcao == 1:
    print ('O valor {} convertido: {} '.format(numero, bin(numero)))
elif opcao == 2:
    print('O valor {} convertido: {}'.format(numero, oct(numero)))    
elif opcao == 3:
    print ('O valor {} convertido: {}'.format(numero, hex(numero)))  
else:
    print('É obrigatório escolher uma das sentenças 1,2,3.') 

#desafio numerico

numero1 = float(input('Digite um valor: '))
numero2 = float (input('Digite o segundo valor: '))

if numero1 == numero2 :
    print('Os numeros são equivalentes')
elif numero1 != numero2 and numero1 > numero2:
    print('''Os valores são diferentes:
    Portanto o {} é maior que o {}. '''.format(numero1, numero2))  
elif numero2 != numero1 and numero2 > numero1:
    print(''' Os valores são diferentees :
    Portanto o {} é maior que o {}.'''.format(numero2, numero1))
else :
    print('Por favor, apenas números')          

#próximo
    
from datetime import date

atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = atual - nascimento

if idade == 18 or idade == 17:
    print('Procure uma junta militar e aliste-se')
elif idade < 18:
    idade_correta = 18 - idade
    print('Faltam ainda {} anos para o alistamento obrigatório'.format(idade_correta))   
else:
    print ('Por favor procure uma junta militar administrativa e pague a taixa.') 




#outro desafio

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura **2

print ('devido seu peso {:.2f} e sua altura {:.2f}'.format(peso, altura))
print ('Seu imc é: {:.2f}'.format(imc))

if imc <= 18.5:
    print('Você esta abaixo do peso recomendado')

elif imc >18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc <30:
    print('Levimente sobrepeso')
elif imc >30 and imc <40:
    print('Obesidade')

else:
    print('Obesidade mórbida')







