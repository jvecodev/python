class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20
        
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print('Volume máximo atingido')
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print('Volume mínimo atingido')

    def mudar_canal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal
        else:
            print('Canal não disponível')

    def adicionar_canal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentar_volume(self):
        self.tv.aumentar_volume()

    def diminuir_volume(self):
        self.tv.diminuir_volume()

    def mudar_canal(self, canal):
        self.tv.mudar_canal(canal)

    def adicionar_canal(self, canal):
        self.tv.adicionar_canal(canal)