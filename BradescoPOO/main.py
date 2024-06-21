
class main:
    pass
from classes import Cliente

from conta import Conta

print("Bem-vindo ao Bradesco!")

nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
idade = int(input("Digite sua idade: "))
cliente = Cliente(nome, cpf, idade)

Conta.saldo = float(input("Digite o saldo da conta: "))
Conta._titular = cliente._nome

print(f"Cliente: {cliente._nome}, CPF: {cliente._cpf}, Idade: {cliente._idade}")
print(f'Saldo: {Conta.saldo}, Titular: {Conta._titular}')

