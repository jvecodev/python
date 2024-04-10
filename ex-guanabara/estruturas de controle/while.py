pergunta2 = 'S'
pergunta3 = 0
while pergunta2 == 'S':
    valor = int(input('Digite um valor: '))
    pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
    if pergunta2 != 'S' and pergunta2 != 'N':
        pergunta3 = str(input('Não compreendo, digite novamente:'))
        pergunta2 = str(input('Quer continuar [S/N]: ')).upper()
       
print('Fim')

#questionario

sexualidade = str(input('Informe sua sexualidade [M/F]: ')).strip().upper()[0]
while sexualidade not in 'MmFf':
    print('Dado invalidade')
    sexualidade = str(input('Por favor, informe novamente: ')).strip().upper()[0]
print ('Sexo {} resgistrado com sucesso.'.format(sexualidade))


 


    