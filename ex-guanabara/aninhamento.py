casa = float(input('Qual será o valor da sua residência? '))
salario = float(input('Quanto é o seu soldo? '))
parcelas = int(input('Em quantas anos? '))
prestacao = casa/(parcelas*12)
minimo = 0.30*salario

print('Para pagar uma casa de {:.2f} em {} anos, a prestação será de R${:.2f} '.format(casa, parcelas, prestacao))

if prestacao <= minimo:
    print('Emprétimo concedido')
else:
    print('Empréstimo negado')    

