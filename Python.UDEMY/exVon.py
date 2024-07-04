contador = quantidadeLetras = 0
letras = ''
letras1 = []
letras2 = []
maiorQuantidade = 0 
menorQuantidade = 0
palavra = input('Digite uma palavra: ')

while contador < len(palavra):
    
    letra_atual = palavra[contador]
    quantidadeLetras = palavra.count(letra_atual)
    print(f'A letra {letra_atual} aparece {quantidadeLetras} vezes')
    contador += 1

    if contador == 1:
        maiorQuantidade = quantidadeLetras
        menorQuantidade = quantidadeLetras
        letras1 = letra_atual
        letras2 = letra_atual
    else:
        if quantidadeLetras > maiorQuantidade:
            maiorQuantidade = quantidadeLetras
            letras1 = letra_atual
        elif quantidadeLetras < menorQuantidade:
            menorQuantidade = quantidadeLetras
            letras2 = letra_atual

print(f'A letra que mais aparece é {letras1} com {maiorQuantidade} ocorrências')
print(f'A letra que menos aparece é {letras2} com {menorQuantidade} ocorrências')
  