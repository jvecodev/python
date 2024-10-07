def verificar_palindromo(palavra):
    alfanumerico = 'abcdefghijklmnopqrstuvwxyz0123456789'
    minuscula = palavra.lower()
    revisada = ''
    
    for letra in minuscula:
        if letra in alfanumerico :
            revisada += letra
            
    if revisada == '':
        print('Palavra fora das normas alfanuméricas. Digite novamente.')
        print('-' * 10)
        return

    if revisada == revisada[::-1]:
        print(f'{palavra}  é um palindromo!')
    else:
        print(f'{palavra} não é um palindromo!')

palavra_user = str(input('Digite uma palavra: '))
verificar_palindromo(palavra_user)