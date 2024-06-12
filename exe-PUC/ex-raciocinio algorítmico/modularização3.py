# def anotar_altura(quantidade_alunos):
#     alturas = []
#     for cont in range(0, quantidade_alunos):
#         altura = float(input("Digite a altura do aluno " + str(cont + 1) + ": "))
#         alturas.append(altura)
#     return alturas

# def maior_altura(alturas):
#     if len(alturas) == 0:
#         return False
#     maior = alturas[0]
#     for cont in range(1, len(alturas)):
#         if alturas[cont] > maior:
#             maior = alturas[cont]
#     return maior

# def menor_altura(alturas):
#     if len(alturas) == 0:
#         return False
#     menor = alturas[0]
#     for cont in range(1, len(alturas)):
#         if alturas[cont] < menor:
#             menor = alturas[cont]
#     return menor

# def media_altura(alturas):
#     if len(alturas) == 0:
#         return False
#     soma = sum(alturas)
#     media = soma / len(alturas)
#     return media

# pergunta_quantidade = int(input("Quantos alunos tem na turma? "))
# alturas = anotar_altura(pergunta_quantidade)
# altura_maior = maior_altura(alturas)
# altura_menor = menor_altura(alturas)
# media = media_altura(alturas)

# print(f'A maior altura da turma é: {altura_maior}, a menor altura é: {altura_menor} e a média de altura é: {media}')

#Conta bancaria
# usuario = [0] * 3
# def criar_conta(nome, senha, saldo = 0):
#     usuario[0] = nome 
#     usuario[1] = senha
#     usuario[2] = saldo

# nome = input('Digite seu nome: ')
# senha = input('Digite sua senha: ')
# saldo = float(input('Digite o valor que deseja adicionar a sua conta: '))
# criar_conta(nome, senha, saldo)

# def depositar (valor):
#     usuario[2] += valor
#     print(f'Você depositou R${valor} na sua conta')
#     print(f'Seu saldo atual é de R${usuario[2]}')

# def retirar (valor):
#     if usuario[2] < valor:
#         print('Saldo insuficiente')
#     else:
#         usuario[2] -= valor
#         print(f'Você retirou R${valor} da sua conta')
#         print(f'Seu saldo atual é de R${usuario[2]}')

# def menu(lista_opc):
#     for indice, opcao in enumerate(lista_opc):
#         print(f'[{indice+1}] - {opcao}')
#     opcao = int(input('Digite a opção desejada: '))
#     return opcao

# while True:
#     print ('Menu')
#     lista_opcoes = ['Depositar', 'Retirar', 'Imprimir saldo', 'Sair']
#     opcao = menu(lista_opcoes)

#     if opcao == 1:
#         valor = float(input('Digite o valor que deseja depositar: '))
#         depositar(valor)
#     elif opcao == 2:
#         valor = float(input('Digite o valor que deseja retirar: '))
#         retirar(valor)
#     elif opcao == 3:
#         print(f'Seu saldo atual é de R${usuario[2]}')
#     elif opcao == 4:
#         print('Saindo...')
#         break
#     else:
#         print('Opção inválida')
    

def hanoi(discos, origem, destino, temp):
    if discos == 1:
        print("Mova o disco ", discos, " de ", origem, " para ", destino)
    else:
        hanoi(discos - 1, origem, temp, destino)
        print("Mova o disco ", discos, " de ", origem, " para ", destino)
        hanoi(discos-1, temp, destino, origem)
print("Entre com o numero de discos: ")
total_discos = int(input())
hanoi(total_discos,'A','B','C')

    





