# Autor: João Vitor Correa Oliveira

#definindo variáveis para usos futuros 
PreçoPerHora = 5
usuario = [0] * 3
dia = []



def titulo(texto):
    
    print('='*40)
    print(f'  {texto:^35}')
    print('='*40)
titulo('BikePY → Aluguel de bicicletas') 

# Função para cadastro de usuário
def cadastro(nome, email, senha):
    usuario[0] = nome
    usuario[2] = email
    usuario[1] = senha
    if usuario[0] == '' or usuario[1] == '' or usuario[2] == '':
        print('Preencha todos os campos')
        cadastro(input('Digite seu nome: '), input('Digite seu email: '), input('Digite sua senha: '))
        print('Cadastro realizado com sucesso')
    else:
        titulo(f'Bem vind@ {usuario[0]} ao BikePY!')
        titulo('Faça seu login')
    return usuario

def validar_nome2 (nome):
    while nome == '':
        print('Nome inválido, digite um nome válido')
        nome = input('Digite seu nome: ')
    

def validar_nome (nome):
    while nome.isnumeric():
        print('Nome inválido, digite um nome válido')
        nome = input('Digite seu nome: ')
    return nome


    
nome = input('Digite seu nome: ').strip()
nome = validar_nome(nome)
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
cadastro(nome, email, senha)


def login(emailLogin, senhaLogin):
    while True:
        if emailLogin == usuario[2] and senhaLogin == usuario[1]:
            print('Login realizado com sucesso!')
            break 
        
        elif emailLogin != usuario[2] or senhaLogin != usuario[1] :

            print('Email ou senha incorretos tente novamente')
            emailLogin = input('Digite seu email: ')
            senhaLogin = input('Digite sua senha: ')
              
email_login = input('Digite seu email: ')
senha_login = input('Digite sua senha: ')
login(email_login, senha_login)


def validar_crédito(saldo_inicial):
    while True:
        if saldo_inicial < 5:
            print('Saldo insuficiente para alugar bicicleta')
            print()
            saldo_inicial = float(input('Digite novamente um valor que deseja adicionar a sua conta: '))
            print('==================================================')
            
        else:
            print('Créditos adicionados com sucesso!')
            print('Seu saldo atual é de R$', saldo_inicial)
            break
    return saldo_inicial


titulo('Créditos inciais obrigatórios')
print('Preço por hora: R$5,00')
saldo = float(input('Digite o valor que deseja adicionar a sua conta: '))
validar_crédito(saldo)

login(email_login, senha_login)

def menu(lista_opx):
    print()
    for i, opcao in enumerate(lista_opx):
        print(f'[{i+1}] - {opcao}')
    print()
    opcao = int(input('Digite a opção desejada: '))
    return opcao


def perguntar_data():
    dia = 0
    mes = 0
   
    lista = []
    while dia <= 0  or mes <= 0 :
        dia = int(input("Digite o Dia Atual [DD]: "))
        mes = int(input("Digite o Mês Atual [MM]: "))
        
        if dia > 31 or mes > 12 :
            print("ERRO!!! DIA/MÊS INFORMADO INVÁLIDO!!!")
            return perguntar_data()	
    lista.append(dia)
    lista.append(mes)
    return lista

def perguntar_horario():
    hora = -1
    minuto = -1
    lista = []
    while hora < 0 or minuto < 0:
        print('Apenas números inteiros são aceitos')
        hora = int(input("Digite as Horas Atuais [DD]: "))       
        minuto = int(input("Digite os Minutos Atuais [MM]: "))
        if  hora > 24 or minuto > 60 or hora < 0 or minuto < 0:
            print("ERRO!!! HORA:MINUTOS INFORMADO INVÁLIDO!!!")
            return perguntar_horario()
    lista.append(hora)
    lista.append(minuto)
    return lista

def calcular_data_em_minutos(dia, mes):
    calculo_data = (dia * 24 * 60) + (mes * 30 * 24 * 60)
    return calculo_data

def calcular_horario_em_minutos(hora, minuto):
    calculo_horario = (hora * 60) + minuto
    return calculo_horario

def calcular_tempo_em_minutos():
    tempo_minutos_inicio =  calcular_horario_em_minutos(horario_inicio[0], horario_inicio[1]) + calcular_data_em_minutos(data_inicio[0], data_inicio[1])
    tempo_minutos_fim = calcular_horario_em_minutos(horario_fim[0], horario_fim[1]) + calcular_data_em_minutos(data_fim[0], data_fim[1])
    tempo_total = (tempo_minutos_fim - tempo_minutos_inicio)
    custo_total = (tempo_total * PreçoPerHora) /60
    print(f'O tempo total do aluguel foi de: {tempo_total} minutos')
    print('O custo total do aluguel foi de R$', custo_total)
    print('Saldo atual: R$', saldo - custo_total)
    return saldo - custo_total










while True:
    titulo("Menu de opções:")
    lista_opcao = ['Alugar Bicicleta', 'Recarregar créditos ', 'Visualizar Histórico', 'Redefinir minha senha', 'Encerrar Programa']
    opcao = menu(lista_opcao)
    
    if opcao == 1:
        if saldo < 5:
            print('Saldo insuficiente para alugar bicicleta')
            print('Recarregue sua conta para alugar bicicleta')
            print('==================================================')
        else:
            
            print('Aluguel de bicicleta')
            print('=============== AVISOS IMPORTANTES ===============')
            print('1 - O aluguel de bicicletas é cobrado por hora')
            print('2 - Necessário ter créditos em sua conta')
            print('3 - O valor do aluguel é de R$5,00 por hora')
            print('==================================================')
            print('Digite a data ')
            print('==================================================')
            data_inicio = perguntar_data()
            print('==================================================')
            horario_inicio = perguntar_horario()
            print('==================================================')
            print('Digite a data do fim do aluguel')
            print('==================================================')
            data_fim = perguntar_data()
            print('==================================================')
            print('Digite o horário do fim do aluguel')
            print('==================================================')
            horario_fim = perguntar_horario()
            titulo('Aluguel de bicicleta realizado com sucesso!')
            print('==================================================')
            print('Data e horário de início do aluguel: ', data_inicio, horario_inicio)
            print('Data e horário de fim do aluguel: ', data_fim, horario_fim)
            print('==================================================')
            print('Calculando o tempo total do aluguel...')
            saldo = calcular_tempo_em_minutos()
            opcao = menu(lista_opcao)
            print('==================================================')
    
   

    if opcao == 2:
        valor_recarga = float(input('Digite o valor que deseja adicionar a sua conta: '))
        saldo += valor_recarga
        print('Créditos adicionados com sucesso!')
        print('Seu saldo atual é de R$', saldo)

    elif opcao == 3:
        print('Seu saldo atual é de R$', saldo)

    elif opcao == 4:
        nova_senha = input('Digite sua nova senha: ')
        usuario[1] = nova_senha
        print('Senha redefinida com sucesso!')

    elif opcao == 5:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')



    
    


        





        

        

