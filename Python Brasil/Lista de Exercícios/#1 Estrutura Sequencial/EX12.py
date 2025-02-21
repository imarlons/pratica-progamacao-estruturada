# EXERCÍCIO 12

# tendo como dados de entrada a altura de uma pessoa. 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# entrada
altura = float(input('Informe a sua altura: '))

# processamento
pesoIdeal = 72.7 * altura - 58


print('Conforme a sua estatura, o seu peso ideal é {:.2f}kg'.format(pesoIdeal))
