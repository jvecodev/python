import random

def decifrar_game(respostaUser):
    opcoes_Computer = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    
    # Escolha aleatória do computador
    escolha_computador = random.choice(list(opcoes_Computer.keys()))
    
    # Imprime as escolhas
    print(f'Escolha máquina → {opcoes_Computer[escolha_computador]}')
    print(f'Escolha Usuário → {opcoes_Computer[respostaUser]}')
    
    # Determinando o vencedor
    if escolha_computador == respostaUser:
        print('Houve um empate')
    elif (escolha_computador == 1 and respostaUser == 3) or \
         (escolha_computador == 2 and respostaUser == 1) or \
         (escolha_computador == 3 and respostaUser == 2):
        print('Vitória da máquina')
    else:
        print('Vitória humana')

# Exibindo o menu
print('========= Menu =========')
print(' 1 - Pedra')
print(' 2 - Papel')
print(' 3 - Tesoura')

# Entrada do usuário
escolha_user = int(input('Digite sua escolha → '))
decifrar_game(escolha_user)
