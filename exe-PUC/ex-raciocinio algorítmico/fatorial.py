# Primeira maneira 
# from math import factorial
# numero = int(input ('Digite o número para calcularmos seu fatorial: '))
# calculo = numero
# fatorial = 1
# while calculo > 0:
#     print(' {} '.format(calculo), end ='')
#     if calculo > 1:
#         print ('X', end='')
#     else:
#         print ('=',end='')
#     calculo -= 1
#     fatorial = factorial(numero)
# print (' {} '.format(fatorial)) 

# # segunda maneira


fatorial = 1
numero = int(input("Digite um numero para calculo do fatorial = "))
if numero >= 1:
    contador = numero
    while contador > 1:
        fatorial = fatorial * contador
        contador = contador - 1
    print("Fatorial = ", fatorial)
else:
    if numero == 0:
        print("Fatorial = ", fatorial)
    else:
        print("Numero negativo!")



    
    
    