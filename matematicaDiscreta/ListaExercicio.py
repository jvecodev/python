import os

os.system('cls')


# 1 ) Criando uym conjunto

# A = {1,2,3,4,5,6}
# print(A)

# lista = ["bananas", "peras", "laranjas", "abacates"]
# B = set(lista)
# print(B)

# lista = ["bananas", "peras", "laranjas", "limões", "bananas", "bananas", "abacates", "laranjas"]
# B = set(lista)
# print(B)

# def getTamanhoLista(lista):
#     return f'{len(lista)}' 

# print(f'A cardinalidade do conjunto B com a classe  é: B = {getTamanhoLista(B)} ')

#Relaçõa de Pertinência

# teste de igualdde 


# subconjunto

# A= {1,2,3,4,5,6}
# print(set().issubset(A))


# C = {2, 3, 4}
# # Todos os subconjuntos possíveis de C
# subconjuntos = [
#     set(),  # conjunto vazio
#     {2},
#     {3},
#     {4},
#     {2, 3},
#     {2, 4},
#     {3, 4},
#     {2, 3, 4}
# ]

# # Testando se cada subconjunto está contido em C
# for subconjunto in subconjuntos:
#     print(f"{subconjunto} é subconjunto de {C}? {subconjunto.issubset(C)}")

# A= {1,2,3} 

# C = {1,2,3,4,5,}

# D = {5,3,4,2,1} 
# # Testando se cada subconjunto está contido em A 

# if A.issubset(C) and A != C:
#     print(f'{A} é subconjunto de {C}')

# else:
#     print(f'{A} não é subconjunto de {C}')

# if D.issubset(C) and D != C:
#     print(f'{D} é subconjunto de {C}')

# else:
#     print(f'{D} não é subconjunto de {C}')



# Testando a união de conjuntos

# A = {1,2,3,4,5} 
# B = {4,5,6,7,8,9,10}  
# print (B.difference(A)) 

# Menu de operacoes com conjuntos



def menu():
    while True:
        print("1 - União")
        print("2 - Intersecção")
        print("3 - Diferença")
        print("4 - Produto Cartesiano")
        print("5 - Subconjunto")
        print("6 - Sair")
        opcao = int(input("Escolha uma opção: "))

        print("="*20)

        if opcao == 1:
            print("União:", uniao(A, B))

        elif opcao == 2:
            print("Intersecção:", interseccao(A, B))

        elif opcao == 3:
            print("Diferença:", diferenca(A, B))
        
        elif opcao == 4:
            ProdutoCartesiano(A, B)

        elif opcao == 5:
            print("1 - Subconjunto")
            print("2 - Subconjunto Próprio")
            print("3 - Voltar")
            opcao2 = int(input("Escolha uma opção: "))
                
    
            print("="*20)

            
            if opcao2 == 1:
                print("Subconjunto:", subconjunto(A, B))
            elif opcao2 == 2:
                print("Subconjunto Próprio:", subconjuntoProprio(A, B))
            elif opcao2 == 3:
                continue
            else: 
                print("Opção inválida")
                continue

            print("="*20)


        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida")
    return opcao

# inicializar as funções

def uniao(A, B):
    return A.union(B)

def interseccao(A, B):
    return A.intersection(B)

def diferenca(A, B):
    return A.difference(B)

def ProdutoCartesiano(A, B):
    print("Produto Cartesiano:")
    for a in A:
        for b in B:
            print(f"({a}, {b})")
    
def subconjunto(A, B):
    return A.issubset(B)

def subconjuntoProprio(A, B):
    return A.issubset(B) and A != B
    
# Inicializar os conjuntos

# List Comprehension para criar os conjuntos, onde x é cada elemento da lista de entrada e int(x) converte x para inteiro, já o split separa os elementos da lista de entrada por espaço em branco unificando cada valor e o set remove os elementos duplicados da lista de entrada e converte a lista para um conjunto. 
A = set(int(x) 
        for x in 
            input("Digite os elementos do conjunto A separados por espaço: ").split())
B = set(int(x) 
        for x in 
            input("Digite os elementos do conjunto B separados por espaço: ").split())

print("="*20)

# Executar o menu
menu()


   


