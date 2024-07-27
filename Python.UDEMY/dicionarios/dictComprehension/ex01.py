produto = {
     'nome': 'p1', 'preco': 50, 'desconto': 5, 'preco_final': 45, 'categoria': 'informatica', 'produtor': 'dell tecnologies'
}

# Para obter todos os items do dicionario, utilizo o metodo items()

# for chave, valor in produto.items():
#     print(chave, valor)

# # Para obter apenas as chave, utilizo o metodo Keys()

# for chave in produto.keys():
#     print(chave)

# # Para obter apenas os valores, utilizo o metodo values()

# for valor in produto.values():
#     print(valor)


# dict Comprenhension, basicamente é uma forma de criar um dicionario de forma mais rapida, e modificar um dicionario ja existente

dict = {
     valor.upper() if isinstance(valor, str) else valor for  valor in produto.values()
}

print(f' Dicionario: {dict}')