class Conta:
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular
    #metodo set →  alterar o valor do atributo


    # def get_saldo(self):
    #     return self._saldo

    # def set_saldo(self, saldo):
    #     if (saldo < 0):
    #         print("Saldo não pode ser negativo")
    #     else:
    #         self._saldo = saldo

    #property
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

saldo = input("Digite o saldo da conta: ")
titular = input("Digite o titular da conta: ")
conta = Conta(saldo, titular)
print(f'Saldo: {conta.saldo}, Titular: {conta._titular}')