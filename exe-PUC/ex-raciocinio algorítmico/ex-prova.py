# lata_tinta = float(50)
# volume = float (5)
# altura = float(input('Digite a altura: '))
# Raio = float (input('Digite o raio: '))
# area_base = 3.14 * Raio**2
# area_lateral = altura * 2 * 3.14 
# area_total = area_base + area_lateral
# litro = area_total/3
# quantidade_lata = litro/volume

# print ('A área total foi de: ', area_total)
# print('Litro: ',litro)
# print ('Latas necessárias: ',quantidade_lata)

#horario
hora_inicial = int(input('Digite a hora inicial: '))
minuto_inicial = int(input('Digite o minuto inicial: '))
hora_final = int(input('Digite a hora final: '))
minuto_final = int(input('Digite o minuto final: '))

hora_trancorrida = (hora_final - hora_inicial) *60
minuto_transcorrido = minuto_final - minuto_inicial
minutos_total = hora_trancorrida + minuto_transcorrido
print('Tempo gasto: ', minutos_total)

#imposto de renda

# salario = float(input('Digite seu salario: '))
# desconto1 = (salario * 0.15)
# desconto2 = (salario * 0.275)
# if salario > 1257.13 and salario <2512.8:
#     salario_final = salario - desconto1
# else:
#     salario_final = salario - desconto2

# print('Seu salario final é de: ', salario_final)        

#triangulo

# segmento1 = float(input('Digite o primeiro segmento: '))
# segmento2 = float(input('Digite o segundo segmento: '))
# segmento3 = float(input('Digite o terceiro segmento: '))

# if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento2 + segmento1:
#     print('Com certeza é um triângulo ')
# else:
#     print('Não trata-se de um triângulo!')    

# if segmento1 == segmento2 and segmento1 == segmento3:
#     print('Equilátero')
# elif segmento1 == segmento2 or segmento1 == segmento3 or segmento3 == segmento2:
#     print('Isóceles')
# else:
#     print('Escaleno')   

#acumulador
# soma = 0 
# contador = 1
# while contador < 11:
#     contador +=1   
#     soma += contador
#     print(f'A soma = {soma}') 


# numero_secreto = 42  
# tentativas = 0
# while True:
#     chute = int(input("Adivinhe o número (entre 1 e 100): "))
#     tentativas += 1
#     if chute == numero_secreto:
#         print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
#         break
#     elif chute < numero_secreto:
#         print("O número secreto é maior.")
#     else:
#         print("O número secreto é menor.")
# print('Fim')    

# Radioativo
contador = 0
tempo = 0
massa = float(input('Digite a massa inicial do material: '))
while massa > 0.5:
    massa = massa/2
    contador+=1
    tempo += 50
print ('Foram necessários em segundos =',tempo)
    










