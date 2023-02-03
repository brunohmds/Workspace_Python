lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

def soma_listas(lista1, lista2):
    tamanho_menor_lista = min(len(lista1), len(lista2))
    lista_final = []

    for i in range(tamanho_menor_lista):
        lista_final.append(lista1[i] + lista2[i])
        
    return lista_final

lista_somada = soma_listas(lista1, lista2)
print(lista_somada)