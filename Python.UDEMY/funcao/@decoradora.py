# Funcoes decoradoras 

def decoradora(func):
    print('Decoradora')
    
    def interna(*args, **kwargs):
        print('Interna')
        resposta = func(*args, **kwargs)
        return resposta
    return interna


@decoradora

def somar (a, b):
    return a + b

print(somar(1, 2))  # → 3
