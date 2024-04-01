frase = str(input('Digite algo de seu interesse: ')).upper().strip()
print ('A letra (A) aparece  {} vezes.'.format(frase.count('A')))
print ('A primeira letra esta na posição {} '.format(frase.find('A')+1))
print ('A ultima letra apareceu na posição {}'.format(frase.rfind('A')))

#outra 

frase = str(input('Digite seu nome completo: ')).strip()
nome = frase.split()
print ('Seja bem-vindo {}'.format(frase))
print ('Seu primeiro nome é {}'.format(nome[0]))
print ('Seu último nome é {}'.format(nome[len(nome)-1]))




