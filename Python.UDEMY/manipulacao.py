caminho_arquivo = 'C:\\Users\\jccol\\OneDrive\\estudos\\python\\Python.UDEMY\\'
caminho_arquivo += 'manipulacao.txt'

# Abre o arquivo para escrita

# arquivo = open(caminho_arquivo, 'w')


# arquivo.close()\

#contect Manager

with open(caminho_arquivo, 'w') as arquivo:
    print('Arquivo aberto para escrita')
    arquivo.write('Linha 1\n')	
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')
    print('Arquivo fechado')    

