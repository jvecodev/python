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
    
    print('[1] Usuário')
    print('[2] Administrador')
    print('[3] Sair')
    # Serviços oferecidos 
    opcao = input('Qual sua opção de acesso ? ').strip()

    if opcao == '1':
        nome = str(input('\nDigite seu nome: '))
        print('=-'*30)
        print ('Bem vindo {}, esta é a sua chave de usuário: 121212'.format(nome))
        print('=-'*30) 
        #senha digitada
        while menu_usuario:
            chave = input('Digite a chave fornecida: ').strip()
            while contador <=3:
                if chave == '121212':
                    # Entrada permitida
                    print('=== SERVIÇO AO USUÁRIO ===')
                    contador = 0
                    while menu:
                        adicional = True 
                        
                        # Escolha ao menu
                    
                        print('[1] Usar cartão.')
                        print('[2] Recarga.')
                        print('[3] Sair')
                        print('=-'*30)
                        opcao_usuario = input('Digite sua opção: ').strip()
                        if opcao_usuario == '1':
                            if saldo < valor_passagem:
                            
                                print('SALDO INSUFICIENTE DE: R${}'.format(saldo ))
                                print('Recarregue imediatamente')
                                print('=-'*25)
                            else:
                                print('Utilizado com sucesso')
                                saldo -= valor_passagem
                                print('Saldo de atual com decrescimo = ', saldo)  
                        elif opcao_usuario == '2':
                            while adicional:
                                valor_recarga = input('Digite o valor desejado: ')
                                if valor_recarga.isalpha():
                                    print('Por favor, números!')
                                    print('Tente novamente')
                                    continue
                                if valor_recarga:
                                    adicional = True
                                    print ('======= Cartões ↓ =======')
                                    print('[1] Crédito')
                                    print('[2] Débito')
                                    formato = input('Qual a forma de pagamento: ')
                                    if formato:
                                        if formato == '1':
                                            print ('Cartão de crédito')
                                            senha_cartao = input('Digite a senha: ')
                                            print('Conta com senha: ***',senha_cartao)
                                            saldo += float(valor_recarga)
                                            print('Recarregado com sucesso, saldo atual de ',saldo)
                                            adicional = False

                                        elif formato == '2':
                                            print ('Cartão de débito')
                                            senha_cartao = input('Digite a senha: ')
                                            print('Conta com senha: ***',senha_cartao)
                                            saldo += float(valor_recarga)
                                            print('Recarregado com sucesso, saldo atual de ',saldo)
                                            adicional= False     
                                            
                                        else:
                                            print ('\nCartão não vinculado.')
                                            print ('Tente novamente')
                                            print ('=-'*25)
                                            adicional = False

                                            
                                        
                                        
                                else:
                                    print("\nCaracter não identificado.")
                                    print("Tente novamente.")
                                    print("=-"*25)     
                                continue    

                        elif opcao_usuario == '3':
                            print("=-"*25)
                            print('\nVoltando à pagina inicial.')
                            menu = False
                            menu_administrador = False
                            
                            
                        
                        else:
                            print('tente novamente')
                            continue   
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 4 - contador)
                    if contador == 4:
                        menu_usu = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break
                        
                        
    elif opcao == '2':
        nome = str(input('\nDigite seu nome: '))
        print('=-'*30)
        print ('Bem vindo {}, esta é a sua chave de usuário: 212121'.format(nome))
        print('=-'*30)
        while menu_administrador:
            chave = input('Digite a chave fornecida: ').strip()
            while contador <=3:
                if chave == '212121':
                    # Entrada permitida
                    print('===== SERVIÇO AO ADMINISTRADOR =====')
                    contador = 0
                    while menu:
                        adicional = True
                        # Escolha ao menu
                        print('[1] Alterar valor da passagem: ')
                        print('[2] Ver saldo.')
                        print('[3] Sair')
                        print('=-'*30)
                        opcao_adm = input('Digite sua opção: ').strip()
                        if opcao_adm == '1':
                            nova_passagem = input("\ndigite o valor da passagem")
                            if nova_passagem.isnumeric():
                                valor_passagem = float(nova_passagem)
                                print('Passagem atual:',valor_passagem)
                            else:
                                print('Apenas números')
                        elif opcao_adm == '2':
                            print ('=-'*25)
                            print('Seu saldo atual: ', saldo)    
                            print ('=-'*25)    
                        elif opcao_adm == 3:
                            print ('Retornando ao menu administrativo')
                            menu = False
                            menu_administrador = False
                else:
                    contador +=1
                    print('Erro ao digitar a senha, {}tentativas restantes'.format(3- contador))
                    if contador == 4:
                        menu_usuario = False
                        print('Numero maximo de tentativas.') 
    elif opcao == '3':
        print("\nSistema encerrado.") 
        print('=-'*25) 
        print('======== Volte sempre ========')
    else:
        print('Para prosseguir, apenas opções acimas! ')                     



                        

        

    





                                   
                                    
                                    
                        
                    



                           
                        



                    

                
                    




                    


                
                

    


