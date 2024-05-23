from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
);
def titulo(msg, cor=0):
    tam = len(msg) 
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo(' HelPython Sistema de ajuda ', 2)
    ajuda= str(input('Função ou Biblioteca → '))
    titulo (f'Acessando {ajuda}  com o programa HelPython → ',4)
    help(ajuda)
    opcao = str(input('\033[0;30;41mDeseja continuar? FIM para sair: \033[m'))
    if opcao.upper() == 'FIM': 
        break
titulo('Fim programa',1)
titulo('Volte sempre!',1)


