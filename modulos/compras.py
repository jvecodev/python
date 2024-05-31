from valor import resumo
from dados import leiadinheiro

while True:
    compra = leiadinheiro('Digite o preço: R$: ')
    resumo(compra)

    resposta = str(input('Quer continuar? [S/N]: ').upper().strip())
    
    if resposta in 'N':
        break
print('FIM DO PROGRAMA')