import json

#JSON.DUMP() -> Converte um dicionário em um arquivo JSON
#JSON.LOAD() -> Converte um arquivo
#JSON.DUMPS() -> Converte um dicionário em uma string JSON
#JSON.LOADS() -> Converte uma string JSON em um dicionário
# indent=4 -> identa o arquivo JSON com 4 espaços em branco
# ensure_ascii=False -> Permite a escrita de caracteres especiais
# Todos os numeros em json são considerados number, mas quando tranformado em arquivo Py novamente eles, a linguagem irá ler corretamente.


# Criando um dicionário
dicionario = {
    "nome": "Otávio",
    "sobrenome": "Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "Endereço":[
        {
            "rua": "Av. Carioca",
            "numero": 1000
        }

    ]
    
}
with open("dicionario.json", "w", encoding="utf-8") as arquivo:
    print("Arquivo aberto para leitura")
    json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo fechado")


# Preciso ter um caminho definido para conseguir abrir o arquivo.py

caminho_arquivo = 'C:\\Users\\jccol\\OneDrive\\estudos\\python\\Python.UDEMY\\arquivosJSON\\'
caminho_arquivo += 'dicionario.json'
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    print("Arquivo aberto para leitura")
    dicionario = json.load(arquivo)
    print(dicionario)
    print("Arquivo fechado")