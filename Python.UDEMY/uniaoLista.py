#uniao de lista

def zipper(Estados, cidades):
    for indice in range(len(Estados)):
        print(f'{Estados[indice]} - {cidades[indice]}')
    return 'FIM'

listaEstados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais']
listaCidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
(zipper(listaEstados, listaCidades)) 

# Ou utilizar a biblioteca zip_longest e o módulo itertools

from itertools import zip_longest

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c']

print(list(zip_longest(l1, l2, fillvalue='?')))


# Agora para somar esses valores

def somarLista(lista1, lista2):
    for indice in range(len(lista1)):
        print(lista1[indice] + lista2[indice], end = '  ' )
    return 'FIM'
    
        
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
somarLista(lista1, lista2)

#utilizando o zip 

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

# teste pelo terminal





