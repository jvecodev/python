import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4/3)*math.pi*(self.raio**3)
        return vol

    def area(self):
        ar = 4*math.pi*(self.raio**2)
        return ar
    
bola = Esfera('vermelha', 5)
bola1 = Esfera('azul', 10)

print(f'O volume da esfera é {bola.volume():.2f}')
print(f'A área da esfera é {bola.area():.2f}')

print(f'O volume da esfera é {bola1.volume():.2f}')
print(f'A área da esfera é {bola1.area():.2f}')
