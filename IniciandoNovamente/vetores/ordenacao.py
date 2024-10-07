def ordenar_numeros(lista):
    lista = sorted(lista)
    return lista

numeros = []

for i in range(1, 11):  # Para coletar 10 números
    while True:
        numero = input(f'Digite o {i}º número para a sequência → ')
        
        if numero.isnumeric():
            numeros.append(int(numero))   
            break 
        else:
            print('Entrada inválida! Apenas números são permitidos. Tente novamente.')

# Chama a função para ordenar e exibe a lista ordenada
print('Lista ordenada:', ordenar_numeros(numeros))


    