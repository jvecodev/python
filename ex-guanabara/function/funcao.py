#funcao
# def area(largura, comprimento):
#     a = largura * comprimento
#     print(f'A área de um terreno {largura}x{comprimento} é de {a}m²')
# l = float(input('Largura(m):'))
# c = float(input('Comprimento(m): '))
# area(l, c)

#Escreva
def escreva(msg):
    tam = len(msg) 
    print('~'*tam)
    print(msg)
    print('~'*tam)
frase = str(input('Digite uma frase: '))
escreva(frase)
while True:
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
    else:
        frase = str(input('Digite uma frase: '))
        escreva(frase)
print('Fim do programa')        
