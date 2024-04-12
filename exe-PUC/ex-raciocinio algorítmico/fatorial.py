# Primeira maneira 
from math import factorial
numero = int(input ('Digite o número para calcularmos seu fatorial: '))
calculo = numero
fatorial = 1
while calculo > 0:
    print(' {} '.format(calculo), end ='')
    if calculo > 1:
        print ('X', end='')
    else:
        print ('=',end='')
    calculo -= 1
    fatorial = factorial(numero)
print (' {} '.format(fatorial)) 

# # segunda maneira
# numero = int(input ('Digite o número para calcularmos seu fatorial: '))
# calculo = numero
# fatorial = 1
# while calculo > 0:
#     print(' {} '.format(calculo), end ='')
#     if calculo > 1:
#         print ('X', end='')
#     else:
#         print ('=',end='')
#     fatorial *= calculo
#     calculo -= 1
# print (' {} '.format(fatorial)) 


    
    
    