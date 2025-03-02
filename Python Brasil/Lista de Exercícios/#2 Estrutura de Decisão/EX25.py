# EXERCÍCIO 25

# faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# as perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# o programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def classificarParticipacao():
    perguntas = [
        'Telefonou para a vítima?',
        'Esteve no local do crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima'
    ]
    
    respostasPositivas = 0
    
    for pergunta in perguntas:
        # entrada
        resposta = input(pergunta + ' (sim/não): ').strip().lower()
        if resposta == 'sim':
            respostasPositivas += 1
    
    if (respostasPositivas == 2):
        classificacao = 'Suspeita'
    elif (3 <= respostasPositivas <= 4):
        classificacao = 'Cúmplice'
    elif (respostasPositivas == 5):
        classificacao = 'Assassino'
    else:
        classificacao = 'Inocente'
    # saída
    print('Classificação: ', classificacao)

# chama a função e executa o programa
classificarParticipacao()
