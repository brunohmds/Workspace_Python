cpf_usuario = input("Digite o seu CPF: ")
cpf_limpo = ''
digitos_cpf_int = []

while len(cpf_usuario) != 11 and len(cpf_usuario) != 14:
    cpf_usuario = input("Tentativa errada. Digite novamente: ")
else:
    for digitos in cpf_usuario:
        if digitos in '0123456789':
            cpf_limpo += digitos

    for i in cpf_limpo:
        digitos_cpf_int.append(int(i))
        del (digitos_cpf_int[9:10])

    # Verificando CPF com apenas um número
    sequencia = True
    primeiro_digito = cpf_limpo[0]
    for digitos in cpf_limpo:
        if digitos != primeiro_digito:
            sequencia = False

    # Testando o primeiro dígito verificador
    multiplicador = 10
    soma_primeiro_digito = 0
    for i in range(9):
        soma_primeiro_digito += (digitos_cpf_int[i] * multiplicador)
        multiplicador -= 1

    verifica_primeiro_digito = 11 - (soma_primeiro_digito % 11)
    if verifica_primeiro_digito > 9:
        digitos_cpf_int.append(0)
    else:
        digitos_cpf_int.append(verifica_primeiro_digito)

    # Testando o segundo dígito verificador
    multiplicador = 11
    soma_segundo_digito = 0
    for i in range(10):
        soma_segundo_digito += (digitos_cpf_int[i] * multiplicador)
        multiplicador -= 1

    verifica_segundo_digito = 11 - (soma_segundo_digito % 11)
    if verifica_segundo_digito > 9:
        digitos_cpf_int.append(0)
    else:
        digitos_cpf_int.append(verifica_segundo_digito)

    cpf_comparável = ''
    for i in range(11):
        cpf_comparável += str(digitos_cpf_int[i])

    if cpf_comparável == cpf_limpo and not sequencia:
        print("CPF válido")
    else:
        print("CPF inválido")
