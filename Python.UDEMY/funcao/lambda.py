lista = [
    {
        "nome": "João",
        "idade": 25
    },
    {
        "nome": "Maria",
        "idade": 30
    },
    {
        "nome": "José",
        "idade": 29
    },
    {
        "nome": "Ana",
        "idade": 31
    },
    {
        "nome": "Pedro",
        "idade": 23
    }
]
def ordenarIdade (item):
    return item["idade"]


def ordenarNome (item):
    return item["nome"]
# Recebe a funcao como chave de ordenacao
lista.sort(key = ordenarIdade)
print(lista) # Ordena a lista de acordo com a idade 

lista.sort(key = ordenarNome)
print(lista) # Ordena a lista de acordo com o nome


# Ordenacao pro lambda 
# Uma função lambda é uma função anônima que pode ser definida em uma única linha. 
lista.sort(key = lambda item: item["idade"])
print(lista) # Ordena a lista de acordo com a idade

lista.sort(key= lambda item: item["nome"]) # Ordena a lista de acordo com o nome
print(lista) # Ordena a lista de acordo com o nome