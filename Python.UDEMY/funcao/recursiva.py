# maneira mais simples de se fazer uma funcao de fatorial
# Uma funcao recursiva é uma funcao que chama a si mesma

def fatorial(n):
    if n == 1:
        return 1  # Caso Base
    else:
        return n * fatorial(n - 1)  # Caso Recursivo

print(fatorial(5))  # 120


# uma funcao recursiva pode ser perigosa, pois pode causar um erro de estouro de pilha
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded → Erro de estouro de pilha um limite de seguranca para nao estourar o computador com recursao infinita

# def recursao_infinita():
#     return recursao_infinita()

# recursao_infinita()

