matriz = [[0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0], 
                          ]
for l in range (0,3):
    for c in range (0,5):
        matriz[l] [c]= input(f'Digite um valor para {l}, {c}:  ')

print('='*30)
for l in range(0,3):
    soma = 0
    for c in range(0,5):
        soma += int(matriz[l][c])
        print(f'[{matriz [l][c]:^5}] ',end='→')
    print(f'Soma da linha {l} é {soma}')

# #implementando media
# matriz = [[0, 0, 0, 0], 
#           [0, 0, 0, 0], 
#           [0, 0, 0, 0], 
#                           ]
# nome = ['joao', 'pedro', 'maria']
# for l in range (0,3):
    
#     for c in range (0,4):
#         matriz[l][c]= input(f'Digite um valor para {l}, {c}:  ')

# print('='*30)
# for l in range(0,3):
#     soma = 0
#     for c in range(0,4):
#         soma += int(matriz[l][c])
#         media = soma/4
#         print(f'{nome[l]:^3}{matriz [l][c]:^5} ',end='→ ')
#     print(f'Soma da linha {l} é {soma} e a média é {media}')

# apostas = []
# #faça em formato de tbaela 
# # 
# for resultado in range(5):
#     linha = []
#     for jogos in range(3):
#         jogo = str(input(f'Jogador {resultado+1} | Jogo {jogos+1}: '))
#         linha.append(jogo)
#     apostas.append(linha)

# for resultado in range(5):
#     print(f'Jogador {resultado+1} apostou:')
#     for jogos in range(3):
#          print(f'Jogo {jogos+1}: {apostas[resultado][jogos]}')
         


# matrizA = [0,0] #linhas
# matrizB = [0,0] #linhas
# matrizC = [0,0] #linhas
# for linha in range(0,2):
#     matrizA[linha] = [0,0] #colunas
#     matrizB[linha] = [0,0] #colunas 
#     matrizC[linha] = [0,0] #colunas 
# print('Matriz A')
# for linha in range(0,2):
#     for coluna in range(0,2):
#         matrizA[linha][coluna] = int(input('Digite um valor: '))
# print('Matriz B')
# for linha in range(0,2):
#     for coluna in range(0,2):
#         matrizB[linha][coluna] = int(input('Digite um valor: '))
# for linha in range(0,2):
#     for coluna in range(0,2):
#         matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
# print(matrizC)


matriz_inicDireta = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for linha in range(3):
    print("Linha", linha)
    for coluna in range(3):
        print(matriz_inicDireta[linha][coluna])
for linha in range(2, -1, -1):
    print("Linha", linha)
    for coluna in range(2, -1, -1):
        print(matriz_inicDireta[linha][coluna])