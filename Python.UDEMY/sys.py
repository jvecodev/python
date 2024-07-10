# Essa biblioteca é usada para interagir com o sistema operacional. Ela fornece acesso a algumas variáveis e funções que interagem com o ambiente do sistema operacional.

# import sys
# try:
#     1 / 0
# except ZeroDivisionError:
#     print(sys.exc_info())

# import sys
# print(sys.platform)
# print(sys.version)

# # neste caso, nada abaixo do codigo ira contabilizar pois o programa ira parar

# # import sys
# # sys.exit("Saindo do programa")

# # nesse caso o pograma nao ira parar pois é uma saída padrão
# import sys
# sys.stdout.write("Escrevendo na saída padrão\n")

# Exercicios simples

# def multiplicar(*args):
#     resultado = 1
#     for indice in args:
#         resultado *= indice
#     return resultado

# # Nesse caso aparecera o none pelo existencia do print
# # print(multiplicar(1, 2, 3, 4, 5))
# resposta = (multiplicar(1,2,3,4,5,))
# print(resposta)


# Utilizando High order 
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        numero *= multiplicador
        return numero
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
print(dobro( 2 ))
print(triplo(2))



    
    
