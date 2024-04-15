
saldo = 0
valor_passagem = 0
contador = 0
adcional = True

menu = True
menu_usu = True
menu_usu_1 = True
menu_1 = True
while True:
    adcional = True
    menu = True
    menu_usu = True
    menu_usu_1 = True
    menu_1 = True
    contador = 0
    print("============= Opções de contas =============")
    print("Opções de contas")
    print("1 = Usuário")
    print("2 = Administrador")
    print("3 = Sair")
    print("============================================")
    conta = input("Digite qual conta deseja utilizar: ").strip()

    if conta == "1" :
        print("\nBem vindo a página de login do usuário. ")
        while menu_usu:
            senha1 = input("\nPara continuar, por favor, digite a senha: ")
            while contador <= 2:
                if senha1 == "123456":
                    contador = 0
                    print("\nBem vindo a página do Usuário!")
                    while menu:
                        adcional = True
                        print("\n============== Opções de menu ==============")
                        print("1 = Usar cartão")
                        print("2 = Recarregar saldo")
                        print("3 = sair")
                        print("============================================")
                        opção_menu = input("Digite a opção que deseja utilizar: ").strip()
                        if opção_menu == "1":
                            if saldo < valor_passagem:
                                print("\n============================================")
                                print("\nSaldo insuficiente.")
                                print("\n Seu saldo atual é de:",saldo)
                                print("\n============================================")
                            else:
                                print("\n============================================")
                                print("\nValor da passagem debitado do cartão")
                                saldo -= valor_passagem
                                print("\nSeu saldo atual é de:",saldo)
                                print("\n============================================")
                            continue
                        elif opção_menu == "2":
                            while adcional:
                                add_saldo = input("\nDigite quanto deseja recarregar: ").strip()
                                if add_saldo.isalpha():
                                    print("\nCarácter inválido")
                                    print("Tente novamente.")
                                    print("\n============================================")
                                    continue
                                if add_saldo:
                                    saldo += float(add_saldo)
                                    print("Saldo após a recarga:",saldo)
                                    adcional = False
                                else:
                                    print("\nCaracter não identificado.")
                                    print("Tente novamente.")
                                    print("\n============================================")
                            continue
                        elif opção_menu == "3":
                            print("\n===========================================")
                            print("Voltando para página inicial")
                           
                        else:
                            print("tente novamente")
                            continue   
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 3 - contador)
                    if contador == 3:
                        menu_usu = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break
    elif conta == "2" :
        print("\nBem vindo a página de login do administrador. ")
        while menu_usu_1:
            senha_adm = input("\nPara continuar, por favor digite a senha de administrador: ")
            while contador <= 2 :
                if senha_adm == "123456":
                    contador == 0
                    
                    while menu_1:
                        print("\nBem vindo a página do administrador")
                        print("\n============== Opções de menu ==============")
                        print("1 = definir preço da passagem")
                        print("2 = ver saldo")
                        print("3 = sair")
                        print("============================================")
                        opção_menu = input("Digite a opção que deseja utilizar: ").strip()
                        if opção_menu == "1":
                            while True:
                                change_passagem = input("\ndigite o valor da passagem")
                                if change_passagem.isnumeric():
                                    valor_passagem = float(change_passagem)
                                    if valor_passagem > 0:
                                        break
                                else:
                                    print("\nDigite um número válido.")
                        elif opção_menu == "2":
                            print("============================================")
                            print("\nSaldo atual:",saldo)
                            print("\n============================================")
                        elif opção_menu == "3":
                            menu_1 = False
                            menu_usu_1 = False
                            break
                        else:
                            print("============================================")
                            print("\nOpção inválida.")
                            print("Tente novamente.")
                            print("\n============================================")
                            continue
                    break    
                else:
                    contador += 1
                    print("\nSenha incorreta. Tentativas restantes:", 3 - contador)
                    if contador == 3:
                        menu_usu_1 = False
                        print("\nNúmero máximo de tentativas excedido.")
                        break
                break   
    elif conta == "3":
        print("\nSistema encerrado.")
        break
    else: 
        print("Por favor, escolha entre as opções oferecidas. ")