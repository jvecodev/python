alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789'

while True:
    palavra = input('Digite uma palavra/frase → ')
    minuscula = palavra.lower()
    
    filtrada = ''  # Resetando filtrada a cada nova entrada
    reverso = ''   # Resetando reverso a cada nova entrada
    
    # Verificando se a palavra contém apenas caracteres alfanuméricos válidos
    for letra in minuscula:
        if letra in alfabeto:
            filtrada += letra
            reverso = letra + reverso
    
    if filtrada == '':
        print('Palavra fora das normas alfanuméricas. Digite novamente.')
        print('-' * 10)
        continue
    
    # Comparando palavra filtrada com seu reverso
    if filtrada == reverso:
        print('A palavra digitada é um palíndromo →', palavra)
        print('-' * 10)
        break
    else:
        print('A palavra não é um palíndromo, digite novamente ↓')
        print('-' * 10)
        
print('Fim do programa')
