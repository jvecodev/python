from funcionario import *

funcionario = Funcionario('João', 'jvitor.oliveira1803@gmail.com')

funcionario.cadastro_hora('Janeiro', 100)
funcionario.cadastro_hora('Fevereiro', 200)
funcionario.cadastro_salario_hora('Janeiro', 10)
funcionario.cadastro_salario_hora('Fevereiro', 20)

print(funcionario) # Método especial __repr__ é chamado
print(funcionario.calcula_salario('Janeiro'))
print(funcionario.calcula_salario('Fevereiro'))
print('='*30)

