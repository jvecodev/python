# # Exercicio 2)
def calcular_media(quantidade_elementos):
    nova_lista = [int(input(f'Digite o elemento {i+1}: ')) for i in range(quantidade_elementos)]
    soma = [soma + nova_lista[i] for i in range(quantidade_elementos)]
    media = soma / quantidade_elementos
    return f"A média dos elementos é: {media}"

quantidade_elementos = int(input('Digite a quantidade de elementos: '))
media = calcular_media(quantidade_elementos)

#Exercicio 4)
def valores(x, y):
    soma = (x + y) ** 2
    if x <= 5 and x >= 2 and y >= 2 and y <= 3:
        print(f"Resultado do somatório(x,y) = ({x},{y})", soma)
        return soma  
    else:
        print('Fora da faixa')
        return 0  
soma_total = 0
novos_valores = [valores(x, y) for x in range(2, 6) for y in range(2, 4)]
# temos possibilidades de fazr acumuladores em list comprehension, porem é mais recomendado usar o for tradicional, apenas se usar o list comprehesion e a funcao SUM
for valor in novos_valores:
    soma_total += valor

print("Valores retornados:", novos_valores)
print("Soma de todos os resultados:", soma_total)
################################################################################
def valores1(x, y):
    soma = x*y - 5
    if x <= 3 and x >= 1 and y >= 1 and y <= 2:
        print(f"Resultado do somatório(x,y) = ({x},{y})", soma)
        return soma  
    else:
        print('Fora da faixa')
        return 0  
soma_total = 0
novos_valores = [valores1(x, y) for x in range(1, 4) for y in range(1, 3)]
# temos possibilidades de fazr acumuladores em list comprehension, porem é mais recomendado usar o for tradicional, apenas se usar o list comprehesion e a funcao SUM
for valor in novos_valores:
    soma_total += valor

print("Valores retornados:", novos_valores)
print("Soma de todos os resultados:", soma_total)
################################################################################

#7) ordem invera dos vetores

lista = [3,2,5,7,8,1,4,6,9,10]
print("Lista original:", lista)
lista_inversa = lista[::-1]
print('Conjunto', set(lista))

################################################################################

from random import randint

num = []
def sorteia():
    for i in range (1,7):
        escolha_aleatoria = randint(1,60)
        num.append(escolha_aleatoria)
    return num

def somaPar():
    soma = 0
    pares = [n for n in num if n % 2 == 0]
    [soma := soma + n for n in pares]
    print("Numeros sorteados:", num)
    print("Numeros pares:", pares)
    print("Soma dos numeros pares:", soma)
    return soma


# sorteia()
# somaPar()

################################################################################
#9)


palavra = input("Digite uma palavra: ")
lista = list(palavra)

def descobrir_consoantes(lista):
    consoantes = list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    contador = 0
    verificadas = [letra for letra in lista if letra in consoantes]
    contador = len(verificadas)

    print("Consoantes:", verificadas)
    print("Quantidade de consoantes:", contador)

    return contador

descobrir_consoantes(lista)

################################################################################
#10)

lista_alunos = ['Pedro', 'João', 'Maria', 'Ana', 'José', 'Carlos', 'Paulo']
medias = []
def verificar_media ():
    for i in range (len(lista_alunos)):
        nome = lista_alunos[i]
        notas = [float(input(f'Digite a nota {i+1} do aluno {nome}: ')) for i in range(4)]
        media = sum(notas) / len(notas)
        medias.append(media)
        print(f"A média do aluno {nome} é: {media}")
    return media

def verificar_maior (medias):
    contador = 0 
    maior_que7 =[i for i in medias if i >= 7]
    contador = len(maior_que7)
    print("Alunos com média maior que 7:", maior_que7, "Quantidade de alunos:", contador)

verificar_media()
verificar_maior(medias)

################################################################################
#11)
A = [1,2,3,4,5,6,7,8,9,10]

def verificar_soma_quadrados(A):
    soma = 0
    print ('Lista original,', set(A))
    potencia = [i ** 2 for i in A]
    # é o operador walrus, faz operacoes de acumulação dentro de uma list comprehension
    [soma:= soma + i for i in potencia]
    print('Lista com termos ao quadrado', potencia)
    print('lista de termos com seus quadrados somados: ', soma)

verificar_soma_quadrados(A)
################################################################################
#12)

votos = [0] * 6 

linguagens = ["Python", "C++", "Java", "Rust", "C#", "Outro"]

print("Enquete: Qual a linguagem de programação que tem a melhor tendência para o futuro?")
print("Escolha uma das opções abaixo:")
[print(f"{i+1} - {linguagens[i]}") for i in range(6)]
print("0 - Encerrar a votação\n")

voto = -1
while voto != 0:
    voto = int(input("Informe o número da linguagem (1 a 6) ou 0 para encerrar: "))
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    elif voto != 0:
        print("Valor inválido. Digite um número entre 1 e 6.")
total_votos = 0
# operador walrus novamente, para acumular resultado dentro de uma list comprehension.
[total_votos := total_votos + i for i in votos]

print("\nLinguagem        Votos    %")
print("------------------- -----   ---")
[print(f"{linguagens[i]:<15} {votos[i]:<6} {((votos[i] / total_votos) * 100 if total_votos > 0 else 0):.0f}%") for i in range(6)]
print("------------------- -----")
print(f"Total           {total_votos}")

vencedor_index = votos.index(max(votos))
vencedor = linguagens[vencedor_index]
print(f"\nA linguagem vencedora foi: {vencedor}")

































  







