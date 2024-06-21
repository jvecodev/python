import time
import os

class Cronometro:

    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self):
        return f'{self.horas}:{self.minutos}:{self.segundos}'
    
    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1

        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def start(self):
       while True:
              os.system('cls') # Nao pode usar o clear no windows, apenas em sistemas unix, essa funcao limpa o terminal
              print(self)
              time.sleep(1)
              self.incremento()


cronometro1 = Cronometro()
cronometro1.start()
