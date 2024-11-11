def calcular_sequencia (intervalo):
    valor1 = 0
    valor2 = 1
    
    for i in range(intervalo):
        novo_valor = valor1 + valor2
        valor1 = valor2
        valor2 = novo_valor
        print(valor1, end = '.')
        

escolha_user = int(input('Escolha um valor para a sequencia de fibonacci → '))
calcular_sequencia(escolha_user)
