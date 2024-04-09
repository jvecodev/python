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


'''numero = int(input('Digite o numero da sua taboada: '))
for c in range ( 1,11,):
   print('O resultado de {}x{}={}'.format(numero, c, numero * c))'''





# progressao aritmética
print('='*15)
print('10 termos de uma PA')
print('='*15)

termo = int (input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for c in range (termo,50,razao):
   print (c,'->',end=' ')
print ('Acabou')

#numero primos

numero = int(input('Digite um número: '))
contador = 0
for c in range(1, numero +1):
   if numero % c == 0:
      print ('\033[32m', end='')
      contador =+1
   else:
      print ('\033[31m', end='')
   print ('{}'.format(c),end='')
print ('\n\033[mO {} foi divisível {} vezes'.format(numero, contador))

if contador > 2:
   print('O numero escolhido é PRIMO')
else:
   print ('O numero escolhido não é PRIMO')

#Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]
print ('\033[1;31mO inverso de {} é {} \033[m'.format(junto, inverso))

if junto == inverso:
   print('É um palíndromo')
else:
   print('Não é um palíndromo')  

# outro desafio



       


   




   



   







