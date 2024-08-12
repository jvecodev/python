produtos = [
    {'nome': 'p1', 'preco': 50},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 20},
    {'nome': 'p4', 'preco': 70},
    {'nome': 'p5', 'preco': 90},
    {'nome': 'p6', 'preco': 10},
    {'nome': 'p7', 'preco': 100},
    {'nome': 'p8', 'preco': 80},
    {'nome': 'p9', 'preco': 40},
    {'nome': 'p10', 'preco': 60},
]


# No map, eu posso passar uma função e uma lista, e ele irá aplicar a função em cada item da lista

def aumetarPorcentagem(valor, porcentagem):
    return round (valor * porcentagem, 2)
#round é uma funcão que arredonda numeros, o primeiro valor é o tal numero e o segundo valor são as casas decimais                                    
# 2 = 2 casas decimais

novos_produtos = [
    {**produto, 'preco': aumetarPorcentagem(produto['preco'], 1.05)} for produto in produtos	
]

print(novos_produtos)
print(produtos)

#filtro listcomprehension

maioresProdutos = [
    p for p in produtos 
    if p['preco'] >= 30
]
# desta forma mostrarei apenas produtos maiores que 30

print(maioresProdutos)

# utilizando filter

filterProdutos = filter(
    # É mais ou menos um FOR reduzido, que retorna apenas os valores que são True
    lambda p: p['preco'] >= 30, 
    produtos

)