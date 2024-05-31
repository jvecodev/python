# class Carro:
#     def __init__ (self,marca, potencia, tipo):
#         self.marca = marca
#         self.potencia = potencia
#         self.tipo = tipo

#     def ligar(self):
#         print('Ligando o carro')

#     def acelerar(self):
#         print('Acelerando o carro')

#     def frear(self):
#         print('Freando o carro')

#     def destino(self):
#         print('Cheguei ao meu destino')
#         print('Desligando o carro')

#     def ExibindoInformações(self):
#         print(f'Marca: {self.marca}')
#         print(f'Potência: {self.potencia}')
#         print(f'Tipo: {self.tipo}')
#         print('-------------------------')

# carro1 = Carro ('Ferrari', '760 cavalos', 'Esportivo')
# carro1.ExibindoInformações()
# carro1.ligar()
# carro1.acelerar()
# carro1.frear()
# carro1.destino()

cores = [
    '\033[0;30;41m', # 0 - Vermelho
    '\033[0;30;42m', # 1 - Verde
    '\033[0;30;43m', # 2 - Amarelo
    '\033[0;30;44m', # 3 - Azul
    '\033[0;30;45m', # 4 - Roxo
    '\033[7;30m', # 5 - Branco

]
def titulo (txt, cor = 0):
    tam = len(txt) + 4
    print(cores[cor])
    print('~'*tam)
    print(txt)
    print('~'*tam)
    print(cores[0])
titulo('SISTEMA DE VALIDAÇÃO DE EXPRESSÕES LÓGICAS')



class TabelaVerdade:
    def __init__(self):
        self.matriz = []

    def atribuicaoValoresTabela(self):
        self.matriz = [['V', 'V'], ['V', 'F'], ['F', 'V'], ['F', 'F']]

    def implicacao(self, p, q):
        return (not p) or q

    def conjuncao(self, p, q):
        return p and q

    def bicondicional(self, p, q):
        return p == q
    
    

class Principal:
    def __init__(self):
        self.formula = ''

    def obterFormula(self, cor = 3):
        print(cores[cor])
        self.formula = input('Digite a fórmula: ')
        if self.formula == '':
            print('[RECOMENDAÇÃO] Formato inválido, tente novamente')

        if self.formula == 'p':
            print('[RECOMENDAÇÃO] Falta concluir com outra preposição')

        if self.formula == 'q':
            print('[RECOMENDAÇÃO] Falta concluir com outra preposição')
            print(cores[3])


    def calcularTabelaVerdade(self , cor = 1):

        tabela = TabelaVerdade()
        tabela.atribuicaoValoresTabela()

        for valores in tabela.matriz:
            p = valores[0] == 'V'
            q = valores[1] == 'V'
            resultado = eval(self.formula)

            print(cores[cor], end='')
            print(f'{valores[0]} {self.formula} {valores[1]} = {resultado}')
            print(cores[1], end='')

        while True:
            print('~'*30)           
            continuar = str(input('\033[7;30m Deseja continuar? (s/n) \033[m').upper())
            

            if continuar in 'N':
                break
            
            elif continuar in 'S':

                self.obterFormula()
                self.calcularTabelaVerdade()

principal = Principal()
principal.obterFormula()
principal.calcularTabelaVerdade()
titulo('FIM DO PROGRAMA')




















