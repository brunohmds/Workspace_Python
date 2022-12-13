num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operador = input("Digite qual operador você deseja utilizar: +, -, * ou /: ")

calculadora_ativada = True

while calculadora_ativada:
    try:
        numero_1_float = float(num1)
        numero_2_float = float(num2)
        if operador == "+":
            print("A soma entre os dois números é de:", numero_1_float + numero_2_float)
        elif operador == "-":
            print("A diferença entre os dois números é de:", numero_1_float - numero_2_float)
        elif operador == "*":
            print("A multiplicação entre os dois números é de:", numero_1_float * numero_2_float)
        elif operador == "/":
            print("A divisão entre os dois números é de:", numero_1_float / numero_2_float)
        else:
            print("Operador inválido. Tente novamente.")
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            operador = input("Digite qual operador você deseja utilizar: +, -, * ou /: ")
            continue
        
        sair = input("Você deseja sair? [S]im ou [N]ão? ")
        if sair in "Nn":
            calculadora_ativada = True
            num1 = input("Digite o primeiro número: ")
            num2 = input("Digite o segundo número: ")
            operador = input("Digite qual operador você deseja utilizar: +, -, * ou /: ")
        elif sair in "Ss":
            calculadora_ativada = False
    except:
        print("Valores digitados incorretamente. Tente novamente.")
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        operador = input("Digite qual operador você deseja utilizar: +, -, * ou /: ")
