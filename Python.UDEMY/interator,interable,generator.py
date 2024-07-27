# interator : __iter__(), __next__() → Porém preciso de um interable para utiliza-lo
# interable : __iter__()
# generator : yield (return generator object) → colheitador (iterable), basicamente é uma tupla que dedica menos memória do seu PC, são funções que sabem pausar uma execução e retornar um valor, sem perder o estado da função

import sys

interable = 'Geek'  # interable
interator = iter(interable)  # interator
print(next(interator))
print(next(interator))          # O next só ira funcionar na quantidade exata de letras ou de valores dentro de um interable              
print(next(interator))          # Se eu tentar mais uma vez, dará erro de stopinteration, erro de esgotamento 
print(next(interator))

# for para interable 

interable2 = [ n for n in range(1)]  # interable
print(interable2)  # Desta maneira irá utilizar o devido espaço na memoria do PC

# for para generator
generator = (n for n in range(1))  # generator
for value in generator:
    print(value, end=' → ')  # Printará os valores gerada dentro do generator, sem utilizar o espaço na memoria do PC

# Confirmaremos essa informarção com o sys.getsizeof()

print(f'\n{sys.getsizeof(interable2)} bytes') 
print(f'{sys.getsizeof(generator)} bytes')


# A vantegem de utilizar o generator e com ranges consideralvelmente grandes, pois ele oculpa o mesmo espaço na memoria do PC em qualquer ocasião


def generator(num=0):
    while num <= 10:
        yield num
        num += 1

gen = generator()

for n in gen:
    if n == 10:
        print(n)
    else:
        print(n, end=' → ')

