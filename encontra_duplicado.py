lista_de_listas_de_inteiros =[
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_duplicado(lista):
    for sequencia in lista:
        numeros_checados = []
        duplicado = 0
        numeros_checados.append(sequencia[0])
        
        for i in range(len(sequencia)-1):
            if sequencia[i+1] not in numeros_checados:
                numeros_checados.append(sequencia[i+1])
            elif sequencia[i+1] in numeros_checados:
                duplicado = sequencia[i+1]
                break
    
        if len(numeros_checados) == len(sequencia):
            print(-1)
        else:
            print(duplicado)
                            
encontra_duplicado(lista_de_listas_de_inteiros)