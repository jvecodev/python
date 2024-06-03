try:
    numerador = int(input('Digite o numerador: '))
    denominador = int(input('Digite o denominador: '))
    divisao = numerador / denominador
except ZeroDivisionError:
    print('\033[30;41mNão é possível dividir por zero.\033[m')
except ValueError:
    print('\033[30;42mDigite apenas números inteiros.\033[m')
except Exception as erro:
    print(f'\033[30;43mO erro encontrado foi {erro.__class__}.\033[m')
else:
    print(f'\033[30;44mO resultado da divisão é {divisao}.\033[m')
finally:
    print('\033[31;40mFim do programa.\033[m')
    print('\033[31;40mVolte sempre!\033[m')
    while True:
        try:
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if continuar not in 'SN':
                raise ValueError('Digite apenas S ou N.')
            elif continuar == 'N':
                break
            elif continuar == 'S':
                numerador = int(input('Digite o numerador: '))
                denominador = int(input('Digite o denominador: '))
                divisao = numerador / denominador
                print(f'\033[30;44mO resultado da divisão é {divisao}.\033[m')

                continue
        except ValueError as erro:
            print(f'\033[30;41mO erro encontrado foi {erro}.\033[m')
        else:
            break


