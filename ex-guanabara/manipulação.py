nome = str(input('Digite seu nome: ')).strip()
separa = nome.split()
print('wait')
print('Seu nome em maiúsculas: {} '.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem: {} letras '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], nome.find(' ')))

#outro desafio

numero = int(input('Digite um numero com 4 casas decimais: '))
unidade = numero // 1 %10
dezena = numero // 10 %10
centena =  numero //100 %10
milhar = numero //1000 %10
print('Unidade: ', unidade )
print('Dezena: ', dezena)
print('Centena: ',centena)
print('Milhar:' , milhar)

#outro desafio

city = str(input('Digite a cidade de seu nascimento: ')).strip()
print(city[:5].upper() == 'SANTO')

#outro desafio

nome = str(input('Digite seu nome inteiro: ')).strip()
print ('Seu nome tem Oliveira? {}'.format('OLIVEIRA' in nome.upper()))

#penultimo








