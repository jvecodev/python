print ('---DESAFIO TRIÂNGULO---')

lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

if lado1 <= lado2+lado3 and lado2 <= lado1+lado3 and lado3 <= lado1+lado2:
    print('Os valores {}, {}, {} formam um triângulo' .format(lado1, lado2, lado3)) 
    if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print ('Triângulo equilátero') 
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print ('Triângulo isóceles')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Triângulo escaleno')    
else:
    print('Não será possível formam um triângulo')



   

    