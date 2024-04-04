print('\033[1;36;40m ======lojas Correia======\033[m')
preço_produto = float(input('Digite o preço: '))
print('''Qual é a forma de pagamento
      [1]DINHEIRO
      [2]À VISTA/CARTÃO
      [3]CARTÃO DE CRÉDITO''')
opcao = float(input('Qual sera sua opção? '))

if opcao == 1:
        desconto = preço_produto - (preço_produto * 0.10 )
        print('Valor final: ', desconto)
elif opcao == 2:
        desconto2 = preço_produto - (preço_produto * 0.5)
        print ('Valor final: ',desconto2)
else:
    desconto3 = preço_produto + (preço_produto * 0.5)

print ('\033[1;36;40m ====== Muito obrigado, Volte sempre ======\033[m')


#game

from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')

jogador = int(input('Qual é  deseja: '))
print('-=-'*10)
print ('Jogador jogou: {}'.format(jogador))
print ('COmputador jogou: {}'.format(computador))
print('-=-'*10)

print('Pedra')
time.sleep(.5)
print('Papel')
time.sleep(.5)
print('Tesoura\n')
time.sleep(.5 )


if computador == 0:
    if jogador == 0:
         print('Empate')
        
    elif jogador == 1:
         print('Jogador Venceu')

    elif jogador == 2:
         print('Computador venceu')

    else:
         print ('Jogada invalida')    

if computador == 1:
    if jogador == 0:
         print ('Computador venceu')

    elif jogador == 1:
         print('Empate')

    elif jogador == 2:
         print('O jogador venceu')

    else:
        print ('Jogada invalida')   

if computador == 2:
     if jogador == 0:
          print('Jogador Venceu')  

     elif jogador == 1:
          print('Computador Venceu')

     elif jogador == 2:
          print('Empate')

     else:
          print('Jogada invalidada')               

        
    







    

    

 

