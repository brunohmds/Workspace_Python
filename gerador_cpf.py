import random

nove_digitos = ""
digitos_cpf_int = []

for i in range(9):
    nove_digitos += str(random.randint(0,9))

for i in nove_digitos:
    digitos_cpf_int.append(int(i))

# Adicionando o primeiro dígito verificador
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

# Adicionando o segundo dígito verificador
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

cpf_gerado = ''
for i in range(11):
    cpf_gerado += str(digitos_cpf_int[i])
    if i == 2:
        cpf_gerado += "."
    if i == 5:
        cpf_gerado += "."
    if i == 8:
        cpf_gerado += "-"

print(cpf_gerado)