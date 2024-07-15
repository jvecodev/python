# Jogo da forca

# palavra correta ('python')
# import random

# def escolher_palavra():
#     palavras = ["python", "programacao", "computador", "tecnologia", "desenvolvimento"]
#     return random.choice(palavras)

# def exibir_estado(palavra, letras_corretas):
#     estado = ""
#     for letra in palavra:
#         if letra in letras_corretas:
#             estado += letra + " "
#         else:
#             estado += "_ "
#     return estado

# def jogar_forca():
#     palavra_secreta = escolher_palavra()
#     letras_corretas = set()
#     tentativas = 6
#     letras_erradas = set()

#     print("Bem-vindo ao jogo da forca!")
#     print("Você tem", tentativas, "tentativas para adivinhar a palavra.")

#     while tentativas > 0:
#         print("\nPalavra:", exibir_estado(palavra_secreta, letras_corretas))
#         print("Letras erradas:", " ".join(letras_erradas))
#         chute = input("Digite uma letra: ").lower()

#         if chute in letras_corretas or chute in letras_erradas:
#             print("Você já tentou essa letra.")
#             continue

#         if chute in palavra_secreta:
#             letras_corretas.add(chute)
#             if all(letra in letras_corretas for letra in palavra_secreta):
#                 print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
#                 break
#         else:
#             letras_erradas.add(chute)
#             tentativas -= 1
#             print("Letra incorreta. Você tem", tentativas, "tentativas restantes.")

#         if tentativas == 0:
#             print("Você perdeu! A palavra era:", palavra_secreta)

# jogar_forca()


# Checagem de numeros duplicados


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3,5, 6, 7, 8, 9, 10]	# Lista com números duplicados

# Cria um conjunto vazio para armazenar os números únicos


def checar_duplicados(lista):
    numeros_checados = set()
    duplicados = set()

    for numero in lista:
        if numero in numeros_checados:
            duplicados.add(numero)
        numeros_checados.add(numero)

    return duplicados

print(
    lista,
    f'Números duplicados: {checar_duplicados(lista)}'
)
        



