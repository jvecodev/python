medida = float(input('Digite o altura do seu muro: '))
cm = medida*100
mm = medida*1000
dm = medida*10
hc = medida / 10
km = medida /1000

print ('A medida em cm é: {:.0f} Em mm é:{:.0f} Em dm é: {:.0f} Em hc é: {} E em km é {}'.format(cm,mm,dm,hc,km))

#outro desafio

print ('Desafio da tabuada interativa')


numero = int(input('Digite um numero até 10: '))

print ('-'*12)
print ('{} x {:2}={}'.format(numero,1,numero*1))
print('{} x {:2}={}'.format(numero,2,numero*2))
print ('{} x {:2}={}'.format(numero,3,numero*3))
print('{} x {}={}'.format(numero,10,numero *10))
print ('-'*12)






