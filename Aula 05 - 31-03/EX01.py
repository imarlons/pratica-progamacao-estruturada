# EXERCÍCIO 01

# elabore um algoritmo que dada a idade de um nadador classifica-o em uma das
# seguintes categorias:
# ● infantil A = 5 - 7 anos
# ● infantil B = 8-10 anos
# ● juvenil A = 11-13 anos
# ● juvenil B = 14-17 anos
# ● adulto = maiores de 18 anos

idade = int(input('Informe a sua idade para descobrir a categoria: '))

if (idade < 5):
    print('Você não tem idade suficiente para participar da competição!')
elif (idade >= 5 and idade <= 7):
    print('A sua categoria é INFANTIL A!')
elif (idade >= 8 and idade <= 10):
    print('A sua categoria é INFANTIL B!')
elif (idade >= 11 and idade <= 13):
    print('A sua categoria é JUVENIL A!')
elif (idade >= 14 and idade <= 17):
    print('A sua categoria é JUVENIL B!')
elif (idade >= 18):
    print('A sua categoria é ADULTO!')