caminho_arquivo = 'C:\\Users\\jccol\\OneDrive\\estudos\\python\\Python.UDEMY\\manipulacao\\'
caminho_arquivo += 'manipulacao.txt'

# Abre o arquivo para escrita

# arquivo = open(caminho_arquivo, 'w')


# arquivo.close()\

#contect Manager
                    # Sigla modo de escrita - w
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    print('Arquivo aberto para escrita')
    arquivo.write('Linha 1\n')	
    arquivo.write('Linha 2\n')
    arquivo.write('Atenção → o enconding vai permitir a escrita de caracteres especiais.\n')
    arquivo.write('Linha 4\n')
    print('Arquivo fechado')     

print('='*50)

# para ler o arquivo no terminal 

# with open (caminho_arquivo, 'r') as arquivo:
#     print('Arquivo aberto para leitura')
#     print(arquivo.read())
#     print('Arquivo fechado')

# # agora o A

# with open (caminho_arquivo, 'a') as arquivo:
#     print('Arquivo aberto para escrita')
#     arquivo.write('Linha 5\n')
#     arquivo.write('Linha 6\n')
#     arquivo.write('Linha 7\n')
#     print('Arquivo fechado')

# A diferenca doi A para o W é que o A adiciona as linhas ao final do arquivo, enquanto o W sobrescreve o arquivo, apagando o conteudo anterior

#  Agora o Econding, ele permite que voce leia arquivos com caracteres especiais na sua determina lingua 


    