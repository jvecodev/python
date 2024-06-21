from classes import * # Caracter Coringa que importa todas as classes do arquivo classes.py

tv = Televisor('Samsung', 'UN40K5300')
controle = ControleRemoto(tv)

controle.adicionar_canal('Globo')
controle.mudar_canal('Globo')

print(tv.canal_atual) # Globo