def validar_cpf(cpf):
    cpf = str(cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return "CPF inválido"

    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if cpf[-2:] == f"{digito1}{digito2}":
        return "CPF válido"
    else:
        return "CPF inválido"

print(validar_cpf(10375585370))