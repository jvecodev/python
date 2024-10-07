from classeJson import caminho, Pessoa
import json

# Abrindo o arquivo JSON e carregando a lista
with open(caminho + 'pessoas.json', 'r', encoding='utf-8') as arquivo:
    lista = json.load(arquivo)

    # Instanciando objetos Pessoa apenas com nome e idade
    p1 = Pessoa(lista[0]['nome'], lista[0]['idade'])
    p2 = Pessoa(lista[1]['nome'], lista[1]['idade'])
    p3 = Pessoa(lista[2]['nome'], lista[2]['idade'])

    # Chamando o método get_ano_nascimento para cada instância
    p1.get_ano_nascimento()
    p2.get_ano_nascimento()
    p3.get_ano_nascimento()

    # Exibindo nome e idade
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

# Recriando as instâncias manualmente
p1 = Pessoa('Luiz', 32)
p2 = Pessoa('João', 43)
p3 = Pessoa('Maria', 30)
