import random
import random

captcha = ""
for _ in range(6):
        captcha += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
# Display the captcha
print("Captcha:", captcha)
while True:
    
    resposta = input("Digite o código divulgado: ")
    if resposta == captcha:
        print("Captcha correto, você é humano!")
        break
    else:
        print("Captcha incorreto, tente novamente!")
        for _ in range(1):
            captcha += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            print("Novo Captcha:", captcha)
print('Primeira tentatviva efetuada com sucesso!')
print('=-'*20)
# print('Segunda tentativa!')
# import random

# def gerar_captcha(tamanho=6, caracteres_permitidos="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
#     captcha = ""
#     for _ in range(tamanho):
#         captcha += random.choice(caracteres_permitidos)
# print("Captcha:", captcha)    
# while True:
#     resposta = input("Digite o código divulgado: ")
#     if resposta == captcha:
#         print("Captcha correto, você é humano!")
#         break
#     else:
#         print("Captcha incorreto, tente novamente!")
#         captcha = gerar_captcha()
#         print("Novo Captcha:", captcha)


