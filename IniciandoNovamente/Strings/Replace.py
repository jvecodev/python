def substituição_palavras(letra, simbolo, frase):

    modificacao_frase = frase.title()
    letra_minuscula = letra.lower()

    if letra_minuscula in modificacao_frase:
        modificacao_frase = modificacao_frase.replace(letra_minuscula, simbolo)
        print('Frase ja compilada', modificacao_frase)
    else:
        print('Em nenhum momento apareceu a letra', letra)

simbolo = str(input('Digite o simbolo de substituição → '))
letra = str(input(f'Qual letra deseja modificar para o simbolo → {simbolo}: ' ))
frase = str(input('Digite a frase para haver ou não substituições → '))

substituição_palavras(letra, simbolo, frase)