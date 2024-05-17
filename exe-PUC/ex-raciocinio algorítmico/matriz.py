# matriz = [[0, 0, 0, 0, 0], 
#           [0, 0, 0, 0, 0], 
#           [0, 0, 0, 0, 0], 
#                           ]
# for l in range (0,3):
#     for c in range (0,5):
#         matriz[l] [c]= input(f'Digite um valor para {l}, {c}:  ')

# print('='*30)
# for l in range(0,3):
#     soma = 0
#     for c in range(0,5):
#         soma += int(matriz[l][c])
#         print(f'[{matriz [l][c]:^5}] ',end='→')
#     print(f'Soma da linha {l} é {soma}')

#implementando media
matriz = [[0, 0, 0, 0], 
          [0, 0, 0, 0], 
          [0, 0, 0, 0], 
                          ]
nome = ['joao', 'pedro', 'maria']
for l in range (0,3):
    
    for c in range (0,4):
        matriz[l][c]= input(f'Digite um valor para {l}, {c}:  ')

print('='*30)
for l in range(0,3):
    soma = 0
    for c in range(0,4):
        soma += int(matriz[l][c])
        media = soma/5
        print(f'{nome[l]:^3}{matriz [l][c]:^5} ',end='→ ')
    print(f'Soma da linha {l} é {soma} e a média é {media}')

#