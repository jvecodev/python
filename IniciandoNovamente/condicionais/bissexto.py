def decifrar_ano (ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
        print(f'A ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
    return ano
escolha_ano = int(input('Digite o ano escolhido: '))
decifrar_ano(escolha_ano)