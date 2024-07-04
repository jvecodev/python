# Exemplo de CPF: '123.456.789-09'
cpf = input('Digite o CPF: ')
# Remove os caracteres não numéricos do CPF
cpf = cpf.replace('.', '').replace('-', '')

# Verifica se o CPF tem 11 dígitos
if len(cpf) != 11:
    print("CPF inválido")
else:
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        print("CPF inválido")
    else:
        # Calcula o primeiro dígito verificador
        somaPrimeiro = 0
        for i in range(9):
            somaPrimeiro += int(cpf[i]) * (10 - i)
            resto = somaPrimeiro % 11
            if resto < 2:
                primeiro_digito = 0
            else:
                primeiro_digito = 11 - resto
        
        
        # Calcula o segundo dígito verificador
        somaSegundo = 0
        for i in range(10):
            somaSegundo += int(cpf[i]) * (11 - i)
            resto2 = somaSegundo % 11
            if resto2 < 2:
                segundo_digito = 0
            else:
                segundo_digito = 11 - resto2
        
        
        # Verifica se os dígitos calculados conferem com os dígitos do CPF
        if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
            print("CPF válido")
        else:
            print("CPF inválido")
