# extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


# while True:
#     numero = int(input('Digite um número: '))
    
#     if numero >= 0 and numero <= 20:
#         print (f'O numero escolhido foi o {extenso[numero]}')
#     else:
#         print('Apenas entre 0 e 20')
#         print('Tente novamente!')
#     opcao = str(input('Quer continuar? [S/N]').strip().upper()[0])
#     if opcao == 'N':
#         break
# print('Obrigado!')

# print ('=-'*20)

extenso = ('Zero','Um','Dois', 'Três')
while True:
    numero = int(input('Digite um numero até 3 : '))
    if numero >= 0:
        print (f'O número escolhido foi: {extenso[numero]}')
    else:
        print('Apenas até 3!')
        print('Tente novamente')  
    opcao = str(input('Quer prosseguir, [S/N]: ').strip().upper())
    if opcao !='N' and opcao != 'S':
        print('Somente os valores permitidos')
        print('Tente novamente')
    elif opcao =='N':
        break
print('Obrigado pela participação')
        

        

print('='*30)    




#sorteio

from random import randint
computador = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('=-'*20)
print (f'O valores sorteados foram: ',end='')

for c in computador:
    print (f'{c}',end=' ')
print (f'\nO maior valor foi {max(computador)}')
print(f'O menor valor foi {min(computador)}')
print('=-'*20)    


contador = 0
numero = (int(input('Digitew um numero: ')),
          int(input('Digitew um numero: ')),
          int(input('Digitew um numero: ')),
          int(input('Digitew um numero: ')))

print('Você digitou os numeros {}'.format(numero))
print (f'O numero 9 aparece {numero.count(9)} vezes')

if 3 in numero:
    print(f'O numero 3 apareceu {numero.index(3)+1} posição!')
else:
    print('O numero 3 não apareceu!')  
print('Os valores/valor pare(s) digitaddos são: ',end=' ')    
for n in numero:
    if n % 2 == 0:
        print(f'{n}')

#COMPRAS
lista = ('Caneta', 2,
         'lapis', 1.50,
         'livro', 45.50,
         'Caderno', 30 )
print('-'*40)
print(f'{"LISTA":^40}')
print('-'*40)

for L in range(0,len(lista)):
    if L % 2 == 0:
        print(f'{lista[L]:.<30}',end=" ")
    else:
        print(f'R$ {lista[L]:>5.2f}')
print('-'*40)        


#vogal


palavras = ('Aprender', 'Fluminense', 'Julia', 'Pai', 'Mãe')
for t in palavras:
    print(f'\nNa palavra {t.upper()} temos: ',end='')
    for l in t:
        if l.lower() in 'aeiou':
            print (f'{l}.',end='')







   


        



 
        


        
        