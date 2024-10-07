def valores(x, y, z, n):
    if x + y + z <= n:
        return (x, y, z)
    
    else:
        return '\033[0;31;44m O último conjunto mostrado apresenta soma maior que n / o sistema acabou \033[m'
    
valorx = int(input('Digite o valor de x: '))
valory = int(input('Digite o valor de y: '))
valorz = int(input('Digite o valor de z: '))
valorn = int(input('Digite o valor de n: '))

menores_n = [
    valores(x, y, z, valorn)
    for x in range(valorx + 1)
    for y in range(valory + 1)
    for z in range(valorz + 1)
]

print('Lista de valores que somados são menores ou iguais a n:', *menores_n, sep=' - ')