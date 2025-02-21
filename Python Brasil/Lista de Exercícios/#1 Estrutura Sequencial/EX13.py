# EXERCÍCIO 13

# tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# para homens: (72.7*h) - 58
# para mulheres: (62.1*h) - 44.7

# entrada
altura = float(input('Informe a sua altura: '))
sexo = str(input('Informe o seu gênero, sendo H = Homem e M = Mulher: '))

# processamento

if (sexo.upper() == 'H'):
    pesoIdeal = 72.7 * altura - 58
else:
    pesoIdeal = 62.1 * altura - 44.7

# saída
print('Conforme a sua estatura, o seu peso ideal é {:.2f}kg'.format(pesoIdeal))
