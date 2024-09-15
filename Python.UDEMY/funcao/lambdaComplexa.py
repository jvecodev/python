def executar_funcao(funcao, x, y):
    return funcao(x, y)

print(
    executar_funcao(lambda x, y: x + y, 2, 3)
)

print(
    executar_funcao(lambda x, y: x * y, 2, 3)
)

print(
    executar_funcao(lambda x, y: x ** y, 2, 3)
)

print(
    executar_funcao(lambda x,y : x / y, int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")))
)


lista = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]
lista2 = sorted(lista)
print(lista2)