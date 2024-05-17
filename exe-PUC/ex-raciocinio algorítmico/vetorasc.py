digito = input('Digite qualquer texto: ').lower()

contadorvogal = 0
contadorspace = 0
for indice in range(len(digito)):
    if digito[indice] == 'a' or digito[indice] =='e' or  digito[indice] =='i' or digito[indice] =='o' or digito[indice] =='u':
        contadorvogal +=1
    if digito[indice] == ' ':
        contadorspace += 1
print('Vogais: ', contadorvogal)
print('Espaços: ', contadorspace )



