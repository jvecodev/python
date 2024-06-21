class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, horas):
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = horas


    def calcula_salario(self, mes):
        if mes not in self.horas or mes not in self.salario_hora:
            print('Mês inexistente')
        else:
            if mes in self.horas and mes in self.salario_hora:
                return f'Mês {mes} → {self.horas[mes] * self.salario_hora[mes]}'
            else:
                print('Mês sem horas ou salário cadastrado')
        
    def __repr__ (self):# Método especial em Python. Ele retorna uma representação de string do objeto.

        print('='*30)
        return f'Funcionario: {self.nome}\nEmail: {self.email}\nHoras Trabalhadas: {self.horas}\nSoldo por Hora: {self.salario_hora}' 
        