contador = 0
while contador <10:
    print('contador', contador)
    contador = contador+1
    print('Acabou, tchau obrigado ')  

#outro desafip

contador = 0
resultado = 0
numero = int(input('Digite o numero da sua taboada: '))

while contador < 11:
    resultado = numero * contador 
    print('Resultado de {}x{}'.format(resultado, contador ))
    contador = contador +1
print ('Fim '*2)  

# teste de temperatura

contador = 1
temperatura = float(input("Digite a temperatura = "))
while temperatura < 0:
    print("Temperatura menor que zero.")
    print('Se agasalhe')
    contador +=1
    temperatura = float(input("Digite a temperatura = "))
print("Temperatura = ", temperatura)
print('Voce tentou conectar {} '.format(contador))

# soma/ cálculo acumulativo
contador = 1
soma = 0
while contador < 11:
    soma = soma + contador
    print('Resultado =', soma)
    contador = contador + 1

print(contador)   

#desafio 02
'''contador = 1
nota = float(input('Digite sua nota: '))

loop = True
while loop:
    if nota >= 6:
        print('Nota válida')
        loop = False

print('Volte sempre ')    

while nota < 6:
    print('Nota invalida')
    nota = float(input('Digite sua nota: '))
    contador += 1
print('Voce tentou conectar {} '.format(contador))'''
nota = float(input("Digite a nota (entre 0 e 10) = "))
while nota < 0 or nota > 10:
    print("Nota invalida. Digite novamente.")
    nota = float(input("Digite novamente (entre 0 e 10) = "))





