real = float(input('Quantos reais vc tem na carteira: '))
dolar = real/5.00
print('-'*9)
print('Com esse valor {:.2f}R$, você conseguirá comprar{:.2f} uss$ '.format(real,dolar))
print('-'*9)

#outro desafio, lata de tinta


altura = float(input('Digite a altura do cilindro em metros: '))
diâmetro = float(input('Digite o diâmetro da base: '))
raio = diâmetro/2
area_base_total = 3.14*raio*2
print ('Raio{} e base{}'.format(raio, area_base_total))

area_lateral = 2*3.14*raio*altura
print('A área total do cilindro é {}metros '.format(area_base_total + area_lateral))

preco_tinta = float(50.00)
vol_tinta = float(5)
umlitro = float(3)
quantidade_lata = float(15)
latas_need = (area_base_total + area_lateral)/quantidade_lata

print('A qauntidade de lata necessária é: ',latas_need)
print ('Valor a pagar será de {:.2f}'.format(preco_tinta*latas_need))






