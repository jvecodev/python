lista = []
lista.append(10)
lista.append(20)
for i in range(len(lista)):  #essa lista esta escrita na realidade para não aparecer os colchetes 
    print(lista[i])


# lista = [[], [],]
# for count in range (5):
#     dados = int(input(f'Digite o {count} valor: '))
#     if dados % 2 == 0:
#         lista[0].append(dados)
#     else:
#         lista[1].append(dados)
# print(lista[0])
# print(lista[1])
# print('='*20)

# lista = [4, 5, 6]
# print()
# for i in range(len(lista)):
#     print(lista[i])
# lista.append(7)
# print()
# for i in range(len(lista)):
#     print(lista[i])

# frutas = ['laranja', 'maça', 'pera', 'banana', 'kiwi', 'maça',
# 'banana']
# print(frutas.count('maça'))
# print(frutas.count('tangerina'))
# print(frutas.index('banana'))
# print(frutas.index('banana',4))
# frutas.reverse()
# print(frutas)
# frutas.append('uva')
# print(frutas)
# frutas.sort()
# print(frutas)
# print(frutas.pop())

# listas = []
# soma = 0

# for i in range(5):
#     notas = float(input('Digite sua nota: '))
#     listas.append(notas)
#     soma += notas

# for i in range(len(listas)):
#     print(listas[i])
# media = soma/5
# print ('Medias =',media)

# for i in range (5):
#     if listas[i] > media:
#         print('Notas maiores que a media: ', listas[i])
   

#exercícios

# vetor =[]


# vetor = []
# for i in range(10):
#     valor = int(input("Digite o valor para a posição {}: ".format(i)))
#     vetor.append(valor)

# elemento_procurado = int(input("Digite o elemento que deseja procurar: "))

# if vetor[i] == elemento_procurado:
#     print("O elemento foi encontrado")
# else:
#         print("O elemento não está no vetor.")

#MEGASENA

# from random import randint

# numeros_sorteio = []
# for _ in range(6):
#     numero = randint(1, 60)
#     numeros_sorteio.append(numero)

# print("\nInsira os números da sua aposta:")
# numeros_aposta = []
# for i in range(6):
#     numero = int(input(f"Número {i+1}: "))
#     numeros_aposta.append(numero)

# print(numeros_sorteio)
# print(numeros_aposta)
# if numeros_aposta == numeros_sorteio:
#     print('Parabéns, você é o novo milionário')
# else:
#     print('Que pena, continue tentando')
# #apenas uma encher linguiça 
# numeros_em_comum = set(numeros_sorteio) & set(numeros_aposta)
# print("\nNúmeros em comum:")
# print(numeros_em_comum)

produtos = []
preco = []
quantidade = []
valorfinal = []
print('=========Mercado Power G=========')
while True:
    #Definindo produto
    produto = str(input('Digite o produto: '))
    produtos.append(produto)

    #Definindo Preço Respectivamente
    precos = float(input('Digite o preço: '))
    preco.append(precos)

    #Definindo Quantidade Respectivamente
    quantidades = int(input('Digite as quantidades: '))
    quantidade.append(quantidades)
    
    opcao = str(input('Inserir mais? [S/N]').upper())
    if opcao in 'N':
        break
faturamento_total = sum(valorfinal)
for i in range(len(produtos)):
    print(f'Produto: {produtos[i]}, Preço: R${preco[i]:.2f}, Quantidade: {quantidade[i]}')

print(f'Faturamento total: R${faturamento_total:.2f}')










    


    
    








    

