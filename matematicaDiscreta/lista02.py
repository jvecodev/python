
import os

os.system('cls')


import matplotlib.pyplot as plt
import numpy as np


# A = 2
# B = 5	
# C = 3
# vetorX = [0, 1, 2, 3, 4, 5]
# vetorY = []

# def funcao1oGrau(a,b,x):
#     for i in range(len(x)):
#         vetorY.append(a*x[i] + b)
#     return f"Para a função de 1º grau f(x) = {a}x + {b} temos os seguitnes valores de x: {x} e y: {vetorY}"
# print(funcao1oGrau(A,B,vetorX))



vetorX = np.arange(-5,5,1)
vetorY = np.sin(vetorX) 
print(vetorX)
print(vetorY)

#aqui estamos criando uma janela (figura)
fig = plt.figure(figsize=(10,10))

#aqui estamos plotando ponto a ponto do vetor x com o respectivo y
plt.scatter(vetorX, vetorY, label = "Função Seno") #define o rótulo do gráfico
plt.xlabel("Eixo X") #define o rótulo do eixo x
plt.ylabel("Eixo Y") #define o rótulo do eixo y
plt.title(" f(x) = sen(x)  ") # define o título do gráfico
plt.legend() #mostra a legenda
plt.grid(True, which='both', linestyle='-', linewidth=0.5) #mostra a grade
plt.axhline(0, color='black',linewidth=1) #mostra a linha horizontal eixo x
plt.axvline(0, color='black',linewidth=1) #mostra a linha vertical eixo y

#aqui chamamos a função para mostrar a janela
plt.show()
