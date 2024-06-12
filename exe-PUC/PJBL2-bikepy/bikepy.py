# Autor: João Vitor Correa Oliveira

#definindo variáveis para usos futuros 
PreçoPerHora = 5
usuario = [0] * 3
dia = []
registro_data = []
registro_hora = []




def inserir_titulo(texto):
    
    print('='*50)
    print(f'  \033[30;42m{texto:^45}\033[m')
    print('='*50)
inserir_titulo('BikePY → Aluguel de bicicletas') 

# Função para cadastro de usuário
def cadastro(nome, email, senha):
    usuario[0] = nome
    usuario[2] = email
    usuario[1] = senha
    if usuario[0] == '' or usuario[1] == '' or usuario[2] == '':
        print('\033[31mPreencha todos os campos\033[m')
        cadastro(input('Digite seu nome: '), input('Digite seu email: '), input('Digite sua senha: '))
        inserir_titulo(f'Bem vind@ {usuario[0]} ao BikePY!')
    else:
        inserir_titulo(f'Bem vind@ {usuario[0]} ao BikePY!')
        print('\033[30;44mFaça seu login\033[m'.center(50))
        print('=========================================')
    return usuario

def validar_nome2 (nome):
    while nome == '':
        print('\033[31mNome inválido, digite um nome válido\033[m')
        nome = input('Digite seu nome: ')
    

def validar_nome (nome):
    while nome.isnumeric():
        print('\033[31mNome inválido, digite um nome válido\033[m')
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
            print()
            print('\033[30;44Login realizado com sucesso!\033[m'.center(60))
            break 
        
        elif emailLogin != usuario[2] or senhaLogin != usuario[1] :

            print('\033[31mEmail ou senha incorretos tente novamente\033[m')
            emailLogin = input('Digite seu email: ')
            senhaLogin = input('Digite sua senha: ')
              
email_login = input('Digite seu email: ')
senha_login = input('Digite sua senha: ')
login(email_login, senha_login)


def validar_crédito(saldo_inicial):
    while True:
        if saldo_inicial < 5:
            print('\033[31mSaldo insuficiente para alugar bicicleta\033[m')
            print()
            saldo_inicial = float(input('Digite novamente um valor que deseja adicionar a sua conta: '))
            print('==================================================')
            
        else:
            print('Créditos adicionados com sucesso!')
            print('Seu saldo atual é de R$', saldo_inicial)
            break
    return True


inserir_titulo('\033[30;42mCréditos inciais obrigatórios\033[m')
print('Preço por hora: R$5,00')
saldo = float(input('Digite o valor: '))
validar_crédito(saldo)



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
            print("\033[31mERRO!!! DIA/MÊS INFORMADO INVÁLIDO!!!\033[m")
            return perguntar_data()	
    lista.append(dia)
    lista.append(mes)
    return lista

def visualizar_historico(dia, hora):
    for data in range(len(dia)):
        print('Data:', dia[data][0], '-', dia[data][1]) 
        print('Horário:', hora[data][0], '-', hora[data][1])
        print('=========================================')
    return menu(lista_opcao)
    

def perguntar_horario():
    hora = -1
    minuto = -1
    lista = []
    while hora < 0 or minuto < 0:
        print('Apenas números inteiros são aceitos')
        hora = int(input("Digite as Horas Atuais [DD]: "))       
        minuto = int(input("Digite os Minutos Atuais [MM]: "))
        if  hora > 24 or minuto > 60 or hora < 0 or minuto < 0:
            print("\033[31mERRO!!! HORA:MINUTOS INFORMADO INVÁLIDO!!!\033[m")
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
    inserir_titulo('Menu de opções:')
    lista_opcao = ['Alugar Bicicleta', 'Recarregar créditos ', 'Visualizar Histórico', 'Redefinir minha senha', 'Encerrar Programa']
    opcao = menu(lista_opcao)
    
    if opcao == 1:
        if saldo <= 5:
            print('\033[31mSaldo insuficiente para alugar bicicleta\033[m')
            print('\033[31mRecarregue sua conta para alugar bicicleta\033[m')
            print('==================================================')
        else:
            
            inserir_titulo('Aluguel de bicicleta')
            print('\033[31m=============== AVISOS IMPORTANTES ===============\033[m')
            print('1 - O aluguel de bicicletas é cobrado por hora')
            print('2 - Necessário ter créditos em sua conta')
            print('3 - O valor do aluguel é de R$5,00 por hora')
            print('==================================================')
            print('Digite a data '.center(50))
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
            inserir_titulo('Aluguel de bicicleta realizado com sucesso!')
            data = [0] * 2
            data [0] = str(data_inicio[0]) + '/' + str(data_inicio[1] )
            data [1] = str(data_fim[0]) + '/' + str(data_fim[1])
            registro_data.append(data)
            horario= [0] * 2
            horario [0] = str(horario_inicio[0]) +	':' + str(horario_inicio[1])
            horario[1] = str(horario_fim[0]) + ':' + str(horario_fim[1])
            registro_hora.append(horario)
            print('==================================================')
            print('Calculando o tempo total do aluguel...')
            saldo = calcular_tempo_em_minutos()
            opcao = menu(lista_opcao)
            print('==================================================')
    
   

    elif opcao == 2:
        inserir_titulo('Recarga de créditos')
        valor_recarga = float(input('Digite o valor que deseja adicionar a sua conta: '))
        saldo += valor_recarga
        print('Créditos adicionados com sucesso!')
        print('Seu saldo atual é de R$', saldo)

    elif opcao == 3:
        inserir_titulo('Histórico de alugueis')
        if len(registro_data) == 0:
            print('Nenhum aluguel realizado até o momento')
        else:
            visualizar_historico(registro_data, registro_hora)
        
    elif opcao == 4:
        inserir_titulo('Redefinir senha')
        nova_senha = input('Digite sua nova senha: ')
        usuario[1] = nova_senha
        print('Senha redefinida com sucesso!')


    elif opcao == 5:
        print('Encerrando o programa...')
        print('Obrigado por usar o BikePY!')
        break

    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')



    
    


        





        

        

