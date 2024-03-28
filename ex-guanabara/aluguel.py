distancia = float(input('Qual foi a distancia percorrida em km? '))
dias = int(input('Quantos dias o usuario fez o uso?'))
custo_diario = float(60.00*dias)
custo_distancia = float(0.15*distancia)

total_pagar = float(custo_diario + custo_distancia)

print('O valor total a ser pago é: ',total_pagar )
