# Primeiro exercício com break
print ('=-'*10)
print('[999] Trata-se da flag de parada ')
numero = 0
contador = soma = 0
while True:
    numero = int(input('\nDigite um número: '))
    if numero == 999:
        # Este termo jogará a proxima ação para fora do laço!
        break 

    contador +=1
    soma += numero
print (f'foram digitados {contador} numeros, cuja a soma é {soma}.')

print('=-'*20)
# Tabuada aleatória
print('\nFlag de parada → Valor negativo')

opcao = 'S'
while opcao == 'S':
    
    numero = int(input('Digite outro numero para vermos a tabuada: '))
    if numero < 0:
        break
    for n in range (1,11):
        print (f'{numero}x{n} = {n*numero}')
    print('=-'*20)
    opcao = str(input('Quer continuar? [S/N] ').strip().upper())

print ('Programa encerrado')    
        


   


