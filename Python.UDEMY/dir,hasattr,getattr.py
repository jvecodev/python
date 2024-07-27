# dir, hasasttr e getattr

# dir -> Retorna uma lista de atributos e metodos de um objeto  Utilizado muitas vezes no debugconsole
# hasattr -> Retorna True se um atributo/metodo existir no objeto
# getattr -> Retorna o valor do atributo de um objeto

string = 'Curso de Python'
metodo = 'upper'


#        obj para verificar   verificacao/metodo
if hasattr(string,             metodo):

    # confirmo se o metodo existe
    print(f'Existe o metodo {metodo}')

    # executo o metodo
    print(getattr(string, metodo)())

else:
    # caso o metodo nao exista
    print('Não existe o metodo')