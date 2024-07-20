# Metodos uteis 
# Dicionarios
# clear() → Limpa o dicionário
# copy() → Copia o dicionário
# fromkeys() → Retorna um dicionário com as chaves e valores especificados
# gerna o valor de uma chave específica
# items() → Retotorna uma lista com uma tupla para cada par chave-valor
# keys() → Retorna uma lista com as chaves do dicionário
# pop() → Remove um item do dicionário
# popitem() → Remove o último item inserido no dicionário
# setdefault() → Retorna o valor de uma chave específica. Se a chave não existir, insere a chave com o valor especificado
# update() → Atualiza o dicionário com novos pares chave-valor

# Muda os valores do dicionaro
dicionario = {'a': 1, 'b': 2, 'c': 3}
# print(dicionario)
# dicionario.update(a = 10, b = 20, c = 30)
# dicionario.update([('a', 100), ('b', 200), ('c', 300)]) # desta forma tabem será possivel 
# print(dicionario)


print(list(dicionario.values())) # Retorna uma lista com os valores do dicionário

# Desempacotamento de dicionários

pessoas  = {
    'nome': 'Joao',
    'sobrenome': 'Silva',
}

dados = {
    'idade': 20,
    'cidade': 'São Paulo'
}

conjunto = {**pessoas, **dados}
#     * → Desempacota o dicionario, separando cada item em tupla
print(*conjunto.items(), 'União de dois dicionários')