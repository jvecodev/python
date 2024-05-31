# def verificando_valor (num, max, min):
#     if num > max and num < min:
        
#         return True
#     else:
#         return False
    
    


# maximo = int(input("Digite o valor máximo: "))
# minimo = int(input("Digite o valor mínimo: "))
# valor = int(input("Digite um valor: "))

# resultado = verificando_valor(valor, maximo, minimo)
# if resultado == True:
#     print("O valor está dentro do intervalo")
# else:
#     print("O valor está fora do intervalo")

# def somar(a, b):
#     soma = a + b
#     return soma

# def subtrair(a, b):
#     subtracao = a - b
#     return subtracao

# def multiplicar(a, b):
#     multiplicacao = a * b
#     return multiplicacao

# def dividir(a, b):
#     divisao = a / b
#     return divisao

# def printarCalculadora(valor1, valor2):
#     print(f'O calculo {valor1} + {valor2} = {somar(valor1, valor2)}')
#     print(f'O calculo {valor1} - {valor2} = {subtrair(valor1, valor2)}')
#     print(f'O calculo {valor1} * {valor2} = {multiplicar(valor1, valor2)}')
#     print(f'O calculo {valor1} / {valor2} = {dividir(valor1, valor2):.2f}')
#     return valor1, valor2

# def escolherOperacao(valor1, valor2, escolha):
#     if escolha == 1:
#         print(f'O calculo {valor1} + {valor2} = {somar(valor1, valor2)}')
#     elif escolha == 2:
#         print(f'O calculo {valor1} - {valor2} = {subtrair(valor1, valor2)}')
#     elif escolha == 3:
#         print(f'O calculo {valor1} * {valor2} = {multiplicar(valor1, valor2)}')
#     elif escolha == 4:
#         print(f'O calculo {valor1} / {valor2} = {dividir(valor1, valor2):.2f}')
#     elif escolha == 5:
#         printarCalculadora(valor1, valor2)
#     else:
#         print('Escolha incorreta.')
#     return valor1, valor2, escolha

# valor1 = float(input('Digite um número: '))
# valor2 = float(input('Digite outro número: '))
# print('[1] - SOMAR')
# print('[2] - SUBTRAIR')
# print('[3] - MULTIPLICAR')
# print('[4] - DIVIDIR')
# print('[5] - TODOS')
# escolha = int(input('Escolha um número de opção: '))
# chamar = escolherOperacao(valor1, valor2, escolha)

# def fatorial (num):
#     fat = 1
#     for i in range(num, 0, -1):
#         fat *= i
#         if i == num:
#             print(f'{i}', end=' x ') 
#         else:
#             print(f'{i}', end=' = ')
#     return fat
# numero = int(input('Digite um número: '))
# (fatorial(numero))

# def fatorial (num):
#     fat = 1
#     for i in range(num, 0, -1):
#         if i > 1:
#             print (f'{i} ', end='x ')
#         else :
#             print(f'{i} ', end='= ')
#         fat *= i    
#     return fat
# numero = int(input('Digite um número: '))
# print(fatorial(numero))

# def maior (*num):
#     print('Analisando os valores... ')
#     contador = maior = 0
#     while True:
#         contador += 1
#         n = int(input(f'Digite {contador}° número: '))
        
#         if contador == 1:
#             maior = n
#         else:
#             if n > maior:
#                 maior = n
#         resp = str(input('Quer continuar? [S/N]')).upper()
#         if resp == 'N':
#             break
#     print(f'Você digitou {contador} números e o maior valor foi {maior}')
# maior()

print()
def criptografando(texto):
    texto = texto.lower()
    cripto_texto = ""
    
    for letra in texto:
        if letra == 'a':
            cripto_texto += 'd'
        if letra == 'e':
            cripto_texto += 'h'
        if letra == 'i':
            cripto_texto += 'l'
        if letra == 'o':
            cripto_texto += 'r'
        if letra == 'u':
            cripto_texto += 't'
        else:
            cripto_texto += letra

    return cripto_texto

    
    # if 'a' in texto:
    #     texto = texto.replace('a', 'd')
    # if 'e' in texto:
    #     texto = texto.replace('e', 'h')
    # if 'i' in texto:
    #     texto = texto.replace('i', 'l')
    # if 'o' in texto:
    #     texto = texto.replace('o', 'r')
    # if 'u' in texto:
    #     texto = texto.replace('u', 't')
    
    # return texto
frase = input('Digite uma frase: ')
print(criptografando(frase))

