def verificar_CPF(numCPF):
    soma = 0
    for cont_digito in range(9):
        soma += numCPF[cont_digito] * (10 - cont_digito)
    soma = 11 - (soma % 11)
    if soma > 9:
        soma = 0
    if soma != numCPF[9]:
        print("Problema 1o digito")
        return False
    soma = 0
    for cont_digito in range(10):
        soma += numCPF[cont_digito] * (11 - cont_digito)
    soma = 11 - (soma % 11)
    if soma > 9:
        soma = 0
    if soma != numCPF[10]:
        print("Problema 2o digito")
        return False
    return True

CPF = [0,0,1,2,3,4,5,6,7,9,7]
result = verificar_CPF(CPF)
if result == True:
    print("CPF válido")
else:
    print("CPF inválido")

