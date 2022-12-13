palavra_secreta = "empolgou"
letras_acertadas = ""
quantidade_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    quantidade_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite somente uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_acertada = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_acertada += letra
        else:
            palavra_acertada += "*"
    
    print ("Palavra certa:", palavra_acertada)
    
    if palavra_acertada == palavra_secreta:
        print("Parabéns, você acertou! A palavra secreta era:", palavra_secreta)
        print("Quantidade de tentativas:", quantidade_tentativas)
        break
