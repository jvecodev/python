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

#apenas um teste

codigo = int(input('Digite seu cpr por favor: '))


print('Ultimos digitos: {}'.format(codigo[len(codigo)-4]))



