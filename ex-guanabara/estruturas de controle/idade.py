'''from datetime import date
maiores = 0
for c in range(0,7):
    idade = int(date.today().year - int(input('Digite o ano de nascimento: ')))
    if idade >= 18:
        maiores += 1
print('Entre essas 7 pessoas existem {} maiores e {} menores.'.format(maiores, 7 - maiores))'''


maior = 0
menor = 0 
for c in range (1,8):
    peso = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor :
            menor = peso 
print('O maior peso lido é {}'. format(maior)) 
print('O menor peso lido é {}'.format(menor ))             

#grupo formado
mediaidade = 0
somaidade = 0
maioridade = 0
nomevelho = ''
contador = 0

for c in range (1,5):
    print('====={} PESSOA====='.format(c))
    nome = str(input('Digite seu nome: ' )).strip()
    idade = int(input('Digite sua idade: '))
    sexualidade = str(input('Sexo [M/F]:  ')).strip()
    somaidade += idade
    if c == 1 and sexualidade in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexualidade in 'Mm' and idade > maioridade:
            maioridade = idade
            nomevelho = nome
    if idade < 20 and sexualidade in 'Ff':
         contador += 1
    mediaidade = somaidade / 4         
print('essa é a media das idades {}'.format(mediaidade)) 
print ('O home mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print ('Tem no total {} mulheres abaixo de 20 anos'.format(contador ))
  




   