tarefas = []
tarefas_apagadas = []

def listar_tarefas(lista):
    print("TAREFAS:")
    for i in range(len(lista)):
            print(lista[i])
    print()

while True:
    print("Comandos: listar, desfazer, refazer")
    comando = input("Digite uma tarefa ou comando: ")

    print()

    if comando == 'listar':
        listar_tarefas(tarefas)
    
    elif comando == 'desfazer':
        if len(tarefas) == 0:
            print("Nenhuma tarefa para desfazer")
            print()
            continue
        tarefas_apagadas.append(tarefas.pop())
        listar_tarefas(tarefas)
        
    elif comando == 'refazer':
        if len(tarefas_apagadas) == 0:
            print("Nenhuma tarefa para refazer")
            print()
            continue
        tarefas.append(tarefas_apagadas.pop())
        listar_tarefas(tarefas)
                
    else:
        tarefas.append(comando)
        listar_tarefas(tarefas)
