perguntas = [
    {
        'Pergunta': "Quanto é 2+2?",
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': "Quanto é 5*5?",
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': "Quanto é 10/2?",
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    } 
]

contador = 0

for questoes in perguntas:
    print("Pergunta: " + questoes['Pergunta'])
    print()
    print("Opções:")
    
    for i in range(len(questoes['Opções'])):
        print(str(i) + ") " + questoes['Opções'][i])
    print()
    
    resposta_usuario = input("Escolha uma opção: ")
    try:
        if questoes["Opções"][int(resposta_usuario)] == questoes['Resposta']:
            print("Parabéns! Você acertou")
            contador += 1
        else:
            print("Você errou")
    except:
        print("Você errou")
    print()

print ("Você acertou", contador, "resposta(s) de", len(perguntas), "perguntas.")