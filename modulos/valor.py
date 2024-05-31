# def aumentar (num = 0):
#     porcento = num + (num * 10/100)
#     return porcento

# def diminuir (num = 0):
#     diminuirporcento = num - (num * 10/100)
#     return diminuirporcento

# def dobro (num = 0):
#     dobro = num * 2
#     return dobro

# def metade(num = 0):
#     metade = num/2
#     return metade

def resumo (num):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)  
    porcento = num + (num * 10/100)
    diminuirporcento = num - (num * 10/100)
    dobro = num * 2
    metade = num/2
    
    print(f'Preço analisado: \tR${num:.2f}')
    print(f'A metade: \t\tR${metade:.2f}')
    print(f'O dobro: \t\tR${dobro:.2f}')
    print(f'Aumentando 10%: \tR${porcento:.2f}')
    print(f'Reduzindo 10%: \t\tR${diminuirporcento:.2f}')
    print('-'*35)
   