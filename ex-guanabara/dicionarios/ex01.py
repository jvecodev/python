dados = dict()
dados['aluno'] = str(input('Nome do aluno: '))
dados ['media'] = float(input('Digite a media do aluno: '))
print('-='*30)
print(f'-Nome = {dados["aluno"]} → media = {dados["media"]}' )
if dados['media'] <= 5:
    #neste caso as áspas duplas são necessárias para que o texto seja exibido corretamente
    print(f'{dados["aluno"]} esta REPROVADO')
elif dados['media'] <= 7:
    print(f'dados["aluno"] necessita de recuperação')
else:
    print(f'-{dados["aluno"]} APROVADO COM SUCESSO!')
print('-='*30)

#Sorteio de dados

from random import randint
from operator import itemgetter
from time import sleep
maior = 0
valores = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in valores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rankinkg = sorted (valores.items(), key = itemgetter(1), reverse = True)  # → itemgetter(1) é para ordenar o dicionário pelo valor
print()
print('Ranking dos players ====================')
for i, v in enumerate(rankinkg):
    print(f'{i+1}º Lugar  = {v[0]} com {v[1]}')
    sleep(1)

