lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    tamanho_menor_lista = 0
    if len(lista1) < len(lista2):
        tamanho_menor_lista = len(lista1)
    elif len(lista2) < len(lista1):
        tamanho_menor_lista = len(lista2)
    else:
        tamanho_menor_lista = len(lista1)
    lista_final = []

    for i in range(tamanho_menor_lista):
        tupla_lista = (lista1[i], lista2[i])
        lista_final.append(tupla_lista)

    return lista_final

lista_somada = zipper(lista1, lista2)
print(lista_somada)