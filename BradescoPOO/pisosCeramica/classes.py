class Pisos:
    #preco por metro quadrado
    def __init__(self, cor, preço, largura, comprimento):
        self.cor = cor
        self.preçoM2 = preço
        self.largura = largura
        self.comprimento = comprimento

    def calcularQuantidadeAzulejos(self, area):
        areaAzulejo = self.largura * self.comprimento
        areaNecessaria = area/areaAzulejo
        return areaNecessaria
    
    def calcularPreco(self, area):
        quantidade = self.calcularQuantidadeAzulejos(area)
        preco = quantidade * self.preçoM2
        return preco
    
    def __repr__(self):
        return f'Cor: {self.cor}\nPreço por metro quadrado: {self.preçoM2}\nLargura: {self.largura}\nComprimento: {self.comprimento}\nAzulejos necessários: {self.calcularQuantidadeAzulejos(25)}\nPreço: {self.calcularPreco(25)}\n'
    

    

        
    
