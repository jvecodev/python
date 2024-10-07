import json

caminho = 'C:\\Users\\jccol\\OneDrive\\estudos\\python\\Python.UDEMY\\POO\\'

class Pessoa:
    ano_atual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = self.ano_atual - self.idade

    def get_ano_nascimento(self):
        print(f'Ano de nascimento {self.ano_nascimento}')

# Instanciando as pessoas
p1 = Pessoa('Luiz', 32)
p2 = Pessoa('João', 43)
p3 = Pessoa('Maria', 30)

# Coletando os dicionários de atributos de cada instância
listaPes = [p1.__dict__, p2.__dict__, p3.__dict__]

# Salvando a lista em um arquivo JSON
with open(caminho + 'pessoas.json', 'w') as file:
    json.dump(listaPes, file, indent=4)
