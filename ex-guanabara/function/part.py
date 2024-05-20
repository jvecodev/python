# from datetime import date
# def voto (ano):
#     idade = date.today().year - ano 
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA'
#     elif idade == 16 or idade == 17 or idade == 65:
#         return f'Com {idade} anos: VOTO OPCIONAL'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO'
# nascimento = int(input('Em que ano você nasceu? '))
# print(voto(nascimento))

#fatorial
# def fatorial(num=1):
#     """ Calcula o fatorial de um número
#     :param num: O número a ser calculado
#     :return: O valor do fatorial de um número num
#     """
#     f=1
#     for c in range (num, 0, -1):
#         print(c, end='')
#         if c > 1:
#             print(' x ', end='')
#         else:
#             print(' = ', end='')
#         f *= c
#     return f 
# valor = int(input('Digite um valor para calcularmos seu fatorial: '))
# print(fatorial(valor))  
# help(fatorial)
# print('-='*20)

# def ficha (nome='<desconhecido>',gols=0):
#     print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
# n = str(input('Nome do jogador: '))
# g = str(input('Número de gols: '))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0

# if n.strip() == '' or n.isnumeric() == True:
#     ficha(gols=g)

# else:
#     ficha(n,g)
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return  valor
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')







