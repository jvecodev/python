import time

saldo = 0
valor_passagem = float(6.00)
contador = 0
adicional = True
menu = True
menu_usuario = True
menu_administrador  = True

while True:
    adicional = True
    contador = 0
    menu = True
    menu_usuario = True
    menu_administrador  = True
    
    #abertura
    print('========= Bem-Vindo a Nexus =========')
    print('\n[1] Usuário')
    print('[2] Administrador')
    print('[3] Sair')
    print ('=-'*25)
    opcao = input('Qual sua opção de acesso ? ').strip()

    # Cadastro
    if opcao == '1':
        nome = str(input('\nDigite seu nome: '))
        print('=-'*30)
        print ('Bem vindo {}, esta é a sua chave de usuário: 121212'.format(nome))
        time.sleep(.4)
        print('=-'*30) 

        #senha digitada
        while menu_usuario:
            chave = input('Digite a chave fornecida: ').strip()
            while contador <= 3:
                if chave == '121212':

                    # Entrada permitida
                    print('\n=== SERVIÇO AO USUÁRIO ===')
                    time.sleep(.4)
                    contador = 0
                    while menu:
                        adicional = True 
                        
                        # Escolha ao menu
                        print('[1] Usar cartão.')
                        print('[2] Recarga.')
                        print('[3] Sair')
                        print('=-'*30)
                        opcao_usuario = input('\nDigite sua opção: ').strip()

                        #Usuário decide utilizar o card
                        if opcao_usuario == '1':
                            if saldo < valor_passagem:
                                print('SALDO INSUFICIENTE DE: R${}'.format(saldo ))
                                print('Recarregue imediatamente')
                                print('=-'*25)

                            #Saldo suficiente0
                            else:
                                print('Utilizado com sucesso')
                                saldo -= valor_passagem
                                print('Saldo  atual com decréscimo = ', saldo) 

                        #Usuário necessita de recarga         
                        elif opcao_usuario == '2':
                            while adicional:
                                print ('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
                                valor_recarga = input('\nDigite o valor desejado: ')

                                #Erro
                                if valor_recarga.isalpha():
                                    print('\nPor favor, apenas números!')
                                    print('TENTE NOVAMENTE')
                                    continue

                                #Êxito
                                if valor_recarga:
                                    adicional = True
                                    print ('\n======= Cartões ↓ =======')
                                    print('[1] Crédito')
                                    print('[2] Débito')
                                    formato = input('\nQual a forma de pagamento: ')
                                    time.sleep(.4)

                                    if formato:
                                        if formato == '1':
                                            print ('\nCartão de crédito')
                                            senha_cartao = input('Digite a senha: ')
                                            print('Conta com senha: ***',senha_cartao)
                                            saldo += float(valor_recarga)
                                            print('\nRecarregado com sucesso, saldo atual de ',saldo)
                                            time.sleep(.4)
                                            adicional = False

                                        elif formato == '2':
                                            print ('\nCartão de débito')
                                            senha_cartao = input('Digite a senha: ')
                                            print('Conta com senha: ***',senha_cartao)
                                            saldo += float(valor_recarga)
                                            print('\nRecarregado com sucesso, saldo atual de ',saldo)
                                            time.sleep(.4)
                                            adicional = False

                                        #Senha alfanumérica negada    
                                        else:
                                             if valor_recarga.isalpha():
                                                print('\nPor favor, apenas números!')
                                                print('TENTE NOVAMENTE') 
                                            
                                else:
                                    print("\nCaracter não identificado.")
                                    print("Tente novamente.")
                                    print("=-"*25)     
                                continue   

                        #Usuário decide sair     
                        elif opcao_usuario == '3':
                            print("=-"*25)
                            print('\nVoltando à pagina inicial.')
                            time.sleep(.4)
                            menu = False
                            menu_usuario = False 


                        #Erro na escolha de opções    
                        else:
                            print('tente novamente')
                            continue   

                # Erro ao digitar a senha        
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 4 - contador)
                    if contador == 4:
                        menu_usu = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break

    #Área administrativa        
    elif opcao == '2':
        nome = str(input('\nDigite seu nome: '))
        print('=-'*30)
        print ('Bem vindo {}, esta é a sua chave de usuário: 212121'.format(nome))
        print('=-'*30)

        # Cadastro
        while menu_administrador:
            chave = input('Digite a chave fornecida: ').strip()
            while contador <= 3:
                if chave == '212121':

                    # Entrada permitida
                    print('===== SERVIÇO AO ADMINISTRADOR =====')
                    time.sleep(.4)
                    contador = 0
                    while menu:
                        adicional = True

                        # Escolha ao menu
                        print('[1] Alterar valor da passagem: ')
                        print('[2] Ver saldo.')
                        print('[3] Sair')
                        print('=-'*30)
                        opcao_adm = input('Digite sua opção: ').strip()
                        time.sleep(.4)

                        #ALteração de valor
                        if opcao_adm == '1':
                            nova_passagem = input('\nDigite o valor da passagem:- ')
                            if nova_passagem.isnumeric():
                                valor_passagem = float(nova_passagem)
                                print('Passagem atual R$',valor_passagem)

                            #Valor alfanumérico    
                            else:
                                print('Apenas números')

                        #Vizualização de saldo        
                        elif opcao_adm == '2':
                            print ('=-'*25)
                            print('Seu saldo atual: ', saldo)    
                            print ('=-'*25) 

                        #Serviço efetuado       
                        elif opcao_adm == '3':
                            print ('Retornando ao menu administrativo')
                            time.sleep(.4)
                            adicional = False 
                            menu_administrador = False
                            menu = False 
                # Erro ao digitar a senha             
                else:
                    contador +=1
                    print('Erro ao digitar a senha, {}tentativas restantes'.format(3- contador))
                    if contador == 4:
                        menu_usuario = False
                        print('Numero maximo de tentativas.')
                        break
                break

    #FIM         
    elif opcao == '3':
        print('\n<SISTEMA ENCERRADO>') 
        print('\n======== Volte sempre ========')
        time.sleep(.3)

    #Erro em digitar opções no menu inicial    
    else:
        print('Para prosseguir, apenas opções acimas! ') 
       



                        

    







                                
                                
                                
                    
                



                        
                    



                

            
                




                


            
            




