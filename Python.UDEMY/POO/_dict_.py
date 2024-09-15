class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = self.ano_atual - self.idade

    def get_ano_nascimento(self):
        print(f'Ano de nascimento {self.ano_nascimento}')

p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# #Ober dicionario

print(p1.__dict__)
p1.__dict__['nome'] = 'João'
print(p1.__dict__)

# apagando dado do dict 

del p1.__dict__['nome']
print(p1.__dict__)

#vars 
#vars mostra todos os atributos de uma classe
#vars é uma função que retorna um dicionário com todos os atributos de um objeto

#quando eu usar essa função, ela vai retornar um dicionário com todos os atributos de um objeto, sem precisar usar o __DICT__

print(vars(p1))
# print(vars(p1) == p1.__dict__)







