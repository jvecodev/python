# neste caso o in verifica se a letra 'a' está contida na variável nome
nome = str('Joao')
print('a' in nome)

#Interpolação de strings

#S → String
#D → Inteiro
#F → Float
# % → Modulo
# %s → String
# %d → Inteiro
# %f → Float
# %r → Booleano
#H → Hexadecimal(0x), Octal(0o), Binário(0b)

# Não é muito indicado usar o % para interpolação de strings, pois é uma forma antiga
nome = 'Joao'
idade = 20
print('Meu nome é %s e tenho %d anos' % (nome, idade))  # %s para string e %d para inteiro

# Fatiamento de strings

variavel = 'Olá mundo'

#Fatiamento [inicio:fim:passo]
print(len(variavel))  # len() retorna o tamanho da string
print(variavel[0])  # Retorna a primeira letra da string
print(variavel[-1])  # Retorna a última letra da string
print(variavel[1:])  # Retorna a string a partir da segunda letra
print(variavel[0:4:1])  # Retorna a string do primeiro ao quarto caractere pulando de 2 em 2

# Inverter uma string

print(variavel[::-1])  # Inverte a string



# Trocar ponto por vírgula


# metodos da STR

# capitalize() → Primeira letra maiúscula                             
# title() → Primeira letra de cada palavra maiúscula
# upper() → Todas as letras maiúsculas
# lower() → Todas as letras minúsculas
# strip() → Remove espaços em branco
# lstrip() → Remove espaços em branco do lado esquerdo
# rstrip() → Remove espaços em branco do lado direito
# replace() → Substitui uma string por outra
# split() → Divide a string em uma lista
# join() → Junta uma lista em uma string
# find() → Procura por uma string
# in → Verifica se uma string está contida em outra
# is → Verifica se a string é de um tipo específico

# string = 'joao'
# print(string.zfill(10))  # Adiciona zeros a esquerda	
# print(string.encode())  # Codifica a string

# listaSoma = [1,2,3,4,5,5,6,7,8,9,10]
# print(f'Somando elementos da lista → {sum(listaSoma)}')  # Soma todos os elementos da lista


# Metodos uteis 
# Dicionarios
# clear() → Limpa o dicionário
# copy() → Copia o dicionário
# fromkeys() → Retorna um dicionário com as chaves e valores especificados
# get() → Retorna o valor de uma chave específica
# items() → Retorna uma lista com uma tupla para cada par chave-valor
# keys() → Retorna uma lista com as chaves do dicionário
# pop() → Remove um item do dicionário
# popitem() → Remove o último item inserido no dicionário
# setdefault() → Retorna o valor de uma chave específica. Se a chave não existir, insere a chave com o valor especificado
# update() → Atualiza o dicionário com novos pares chave-valor

# Muda os valores do dicionaro
dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario)
dicionario.update(a = 10, b = 20, c = 30)
dicionario.update([('a', 100), ('b', 200), ('c', 300)]) # desta forma tabem será possivel 
print(dicionario)


