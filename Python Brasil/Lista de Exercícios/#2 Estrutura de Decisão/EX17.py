# EXERCÍCIO 17

# faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# entrada
ano = int(input('Informe um ano para saber se ele é bissexto: '))

# processamento
def anoBissexto(ano):
# um ano é bissexto se for divisível por 4 e não for divisível por 100, exceto se for divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

# saída
if anoBissexto(ano):
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))