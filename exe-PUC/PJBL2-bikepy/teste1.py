

#   Criando listas para armazenar informações
usuario = [0] * 3
registro_data = []
registro_horario = []

#   Preço do serviço por hora
preco_hora = 5

#   inserir_titulo:
#       entrada: titulo
#       saida: cria um titulo personalizado
def inserir_titulo(texto):
    print('=======================================')
    print('     ', texto)
    print('=======================================')

#   menu:
#       entrada: recebe uma lista de opções
#       saída: cria as opções do menu de uma lista, e retorna a opção selecionada
# le a quantidade (len) de coisas que tem na lista e começa a contar + 1 (1,2,3), separa por '-' e imprime a lista
def menu(lista):
    for contador in range(len(lista)):
        print(contador+1, '-', lista[contador])
    print('Digite somente números.')
    opcao = int(input('Digite sua opção: '))
    return opcao

#   criar_conta:
#       entrada: login, senha
#       saída: adiciona a lista usuario a conta criada
def criar_conta(login, senha, creditos):
    usuario[0] = login
    usuario[1] = senha
    usuario[2] = creditos
    print('Usuário cadastrado(a) com sucesso.')

#   segurir_dica_senha:
#       entrada: login do usuário(a) cadastrado(a)
#       saída: dica de senha do usuário(a) cadastrado(a)
def sugerir_dica_senha(login):
    if login == usuario[0]:
        print('A senha começa com:', usuario[1][0])
        print('A senha termina com:', usuario[1][-1])
        return True
    else:
        print('Login não encontrado.')
        return False

#   visualizar_registro:
#       entrada: data e horario
#       saída: Imprimi na tela o histórico
def visualizar_registro(dia, horario):
    for data in range(len(dia)):
        print('Data:', dia[data][0], '-', dia[data][1])
        print('Horário:', horario[data][0], '-', horario[data][1])
        print("=======================================")

#   perguntar_data:
#       entrada: não recebe nenhum parâmetro de entrada
#       saída: retorna uma lista com a data e mês
def perguntar_data():
    dia = 0
    mes = 0
    ano = 0
    lista = []
    while dia <= 0  or mes <= 0 or ano <= 0:
        dia = int(input('Digite o dia atual [DD]: '))
        mes = int(input('Digite o mês atual [MM]: '))
        ano = 2024
        if dia <= 0  or mes <= 0 or ano <= 0:
            print('Dia, mês ou ano informado inválido.')
    lista.append(dia)
    lista.append(mes)
    lista.append(ano)
    return lista

#   perguntar_horario:
#       entrada: não recebe nenhum parâmetro de entrada
#       saída: retorna uma lista com as horas e minutos
def perguntar_horario():
    hora = -1
    minuto = -1
    lista = []
    while hora < 0 or minuto < 0:
        hora = int(input('Digite as horas atuais [HH]: '))
        minuto = int(input('Digite os minutos Atuais [MM]: '))
        if hora < 0 or minuto < 0:
            print('Hora ou minuto informado invalido')
    lista.append(hora)
    lista.append(minuto)
    return lista

#   converter_data_em_minutos:
#       entrada: dia, mês e ano
#       saída: transforma o dia+mês+ano em minutos
def converter_data_em_minutos(dia, mes, ano):
    #   Info:
    #       1 dia = 24h
    #       1 hora = 60 min
    #       1 ano = 12 messes
    #       1 mês = 30 dias
    #   1. (Transforma DIA em horas e horas em minutos)
    #   2. (Transforma MÊS em dias, dias em horas e horas em minutos)
    #   3. (Transforma ANO em messes, messes em dias, dias em horas e horas em minutos)
    #   4. E soma tudo dando a data em minutos.
    calculo = (dia * 24 * 60) + (mes * 30 * 24 * 60) + (ano * 12 * 30 * 24 * 60)
    return calculo                                        

#   converter_horario_em_minutos:
#       entrada: horas, minutos
#       saída: transforma o horario em minutos
def converter_horario_em_minutos(horas, minutos):
    #   Info:
    #       1h = 60min
    return (horas * 60) + minutos

#   transforma_lista_string:
#       entrada: recebe uma lista
#       saída: transforma os itens da lista em str
def transformar_lista_string(lista):
    for contador in range(len(lista)):
        lista[contador] = str(lista[contador])
    return lista

#   Inicio do Programa
#   Registrando o(a) usuário(a), salvando o login, senha e créditos
inserir_titulo('Cadastro | Bikepy')
login = str(input('Login: '))
senha = str(input('Senha: '))
creditos = -1
while creditos < 0:
    creditos = float(input('Digite a quantidade de créditos que gostaria de depositar: R$'))
    if creditos < 0:
        print('Valor informado inválido.')
        print('Tente novamente.')
conta = criar_conta(login, senha, creditos)

opcao = 0
while opcao != 3: # Porque 3? Porque a opção 3 é a opção de encerrar o programa
    #   Menu princial
    inserir_titulo('Menu | Bikepy')
    lista_opcao = ["Login", "Esqueci minha senha", "Encerrar Programa"]
    opcao = menu(lista_opcao)

    if opcao == 1:
        #   Sistema de login com 3 tentativas de login
        for contador in range(3, -1, -1):
            inserir_titulo('Login | Bikepy')
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')
            if login == usuario[0] and senha == usuario[1]:
                break
            else:
                print('Usuário ou senha inválidos.')
                print(f'Tentativas restantes: {contador}')
        if login == usuario[0] and senha == usuario[1]:
            while opcao != 4:
                #   Menu de usuário
                inserir_titulo('Menu Usuário | Bikepy')
                lista_opcao = ["Utilizar Serviço", "Visualizar Histórico", "Recarregar Créditos", "Encerrar Sessão"]
                opcao = menu(lista_opcao)

                if opcao == 1:
                    inserir_titulo('Utilizando o serviço')
                    if usuario[2] >= 5:
                        print('Preço: R$', preco_hora, '| [1 HORA]')
                        print('AVISO: Se o preço ultrapassar alguns minutos será cobrada a diferença.')
                        print('Digite as DATAS e HORÁRIOS no formato correto e somente números.')

                        #   Sistema de utilização do serviço
                        #       Solicitando o dia, mês e ano da retirada da bike
                        print("=======================================")
                        data_inicial = perguntar_data()
                        print("=======================================")
                        horario_inicial = perguntar_horario()
                        inserir_titulo('Entrega da Bike | Bikepy')
                        data_final = perguntar_data()
                        print("=======================================")
                        horario_final = perguntar_horario()

                        #   Transformando a data inicial e final em minutos
                        data_aluguel = converter_data_em_minutos(data_inicial[0], data_inicial[1], data_inicial[2])
                        horario_aluguel = converter_horario_em_minutos(horario_inicial[0], horario_inicial[1])
                        #   Transformando o horário inicial e final em minutos
                        data_devolucao = converter_data_em_minutos(data_final[0], data_final[1], data_final[2])
                        horario_devolucao = converter_horario_em_minutos(horario_final[0], horario_final[1])

                        #   Transformando o horário e data em str
                        data_inicial = transformar_lista_string(data_inicial)
                        data_final = transformar_lista_string(data_final)
                        horario_inicial = transformar_lista_string(horario_inicial)
                        horario_final = transformar_lista_string(horario_final)

                        #   transforma o horario no formato [DD/MM/YYYY] e adiciona no registro_data
                        data = [0] * 2
                        data[0] = data_inicial[0] + '/' + data_inicial[1] + '/' + data_inicial[2]
                        data[1] = data_final[0] + '/' + data_final[1] + '/' + data_final[2]
                        registro_data.append(data)
                        #   transforma a data no formato [DD:MM] e adiciona no registro_horario
                        horario = [0] * 2
                        horario[0] = horario_inicial[0] + ':' + horario_inicial[1]
                        horario[1] = horario_final[0] + ':' + horario_final[1]

                        #   Calculando a diferença de minutos entre o horario inicial e final
                        calcular_minutos = (data_devolucao + horario_devolucao) - (data_aluguel + horario_aluguel)
                        #   Cobra o valor do serviço de 1 hora
                        #   Caso o usuário passe alguns minutos a mais será cobrado a diferença
                        print('=======================================')
                        if calcular_minutos >= 1:
                            registro_horario.append(horario)
                            if calcular_minutos >= 1 and calcular_minutos <= 60:
                                preco_cobrado = preco_hora
                                usuario[2] = usuario[2] - preco_cobrado
                                print('Preço do serviço: R$', preco_cobrado)
                                print('Créditos atuais: R$', usuario[2])
                            elif calcular_minutos > 60:
                                preco_cobrado = (calcular_minutos / 60) * preco_hora
                                usuario[2] = usuario[2] - preco_cobrado
                                print('Preço do serviço: R$', preco_cobrado)
                                print('Créditos atuais: R$', usuario[2])

                        else:
                                print('Data ou horário informado inválido.')
                                print('Voltando ao Menu Usuário.')
                    elif usuario[2] >= 0 and usuario[2] < 5:
                        print('Preço do serviço [1 HORA]: R$', preco_hora)
                        print('Créditos atuais: R$', usuario[2])
                        print('Crédito insuficiente para utilizar o serviço.')
                    if usuario[2] < 0:
                        #   Caso o Usuário fique com Saldo Negativo um aviso será exibido
                        print('Crédito negativo.')
                        print('AVISO: na próxima utilização do serviço será cobrado o valor descontado.')

                elif opcao == 2:
                    #   Imprimi a data e o horario de uso do serviço
                    inserir_titulo('Visualizar Histórico | Bikepy')
                    if len(registro_horario) == 0:
                        print('Nenhum registro encontrado.')
                    else:
                        visualizar_registro(registro_data, registro_horario)

                #   Sistema de deposito de crédito
                elif opcao == 3:
                    inserir_titulo('Recarregar Créditos | Bikepy')
                    creditos = -1
                    while creditos < 0:
                        creditos = float(input('Digite a quantidade de créditos que gostaria de depositar: R$'))
                        if creditos < 0:
                            print('Valor informado inválido.')
                            print('Tente novamente.')
                    usuario[2] = usuario[2] + creditos
                    print('Crédito atual: R$', usuario[2])
                    print('Preço do serviço [1 HORA]: R$', preco_hora)
                elif opcao == 4:
                    print('Encerrando sessão.')
                else:
                    print('Opção inválida. Tente novamente.')

    #   Dica da senha caso o usuário(a) esqueça sua senha dando o primeiro e ultimo digito da senha
    elif opcao == 2:
        inserir_titulo('Dica de Senha | Bikepy')
        login = str(input('Digite seu login: '))
        dica = sugerir_dica_senha(login)
        print('Voltando ao Menu Bikepy.')
    elif opcao == 3:
        print('Encerrando programa.')
    else:
        print('Opção inválida. Tente novamente.')

