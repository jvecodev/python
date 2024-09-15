# import json

# caminho = 'C:\\Users\\luizf\\Documents\\Python.UDEMY\\POO\\'

# class Pessoa:
#     ano_atual = 2024
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.ano_nascimento = self.ano_atual - self.idade

#     def get_ano_nascimento(self):
#         print(f'Ano de nascimento {self.ano_nascimento}')



# p1 = Pessoa('Luiz', 32)
# p2 = Pessoa('João', 43)
# p3 = Pessoa('Maria', 30)

# listaPes = [p1.__dict__, p2.__dict__, p3.__dict__]

# with open (caminho + 'pessoas.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(listaPes, arquivo, indent=4, ensure_ascii=False)

# with open (caminho + 'pessoas.json', 'r', encoding='utf-8') as arquivo:
#     lista = json.load(arquivo)
#     for p in lista:
#         pessoa = Pessoa(p['nome'], p['idade'])
#         print(pessoa.__dict__)
#         pessoa.get_ano_nascimento()
#         print()










