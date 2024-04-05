#from time import sleep 

#ano = int(input('Em que ano estamos?  '))
#proximo_ano = ano + 1
#for count in range(10, -1, -1):
   # print(count)
  #  sleep(.5)
#print('''{} acabou, bom {}
          # BOOM'''.format(ano, proximo_ano))

#OUTRO

'''for count in range(2, 51, 2):
   print(count,end=' ')
print ('Acabou')''' 


numero = int(input('Digite o numero da sua taboada: '))
for c in range ( 1,11,):
   print('O resultado de {}x{}={}'.format(numero, c, numero * c))





# progressao aritmética
print('='*15)
print('10 termos de uma PA')
print('='*15)

termo = int (input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for c in range (termo,50,razao):
   print (c,'->',end=' ')
print ('Acabou')

   







