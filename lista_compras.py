produtos = []

while True:
    print("Selecione uma opção:")
    opcao = input("[i]nserir, [a]pagar ou [l]istar: ")

    if opcao == "i":
        item = input("Digite um item: ")
        produtos.append(item)

    elif opcao == "a":
        indice_para_apagar = input("Digite uma posição para apagar: ")
        try:
            indice = int(indice_para_apagar)
            produtos.pop(indice - 1)
        except:
            print("Não foi possível apagar esse produto. Tente novamente.")

    elif opcao == "l":
        if len(produtos) == 0:
            print("Nada para listar")
        for i in range(len(produtos)):
            print(i + 1, produtos[i])
            
    else:
        print("Opção inválida. Tente novamente")
