def calcular_imc(peso, altura):
    while True:
        if peso > 0 and altura > 0:
            return peso / (altura ** 2)
        
        else:
            print('Valores inválidos')
            peso = float(input('Digite o peso: '))
            altura = float(input('Digite a altura: '))
            

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = calcular_imc(peso, altura)
print(f'O IMC é {imc:.2f}')

print('==================================================')

#contador de palavras em um texto
def contador_palavras(texto):
    count = 0
    for letra in texto:
        if letra == ' ':
            count += 1
    return count 

texto = input('Digite um texto: ')
resultado = contador_palavras(texto)
print(f'O texto tem {resultado} palavras')


