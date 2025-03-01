# EXERCÍCIO 18

# faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime

# entrada
data = input('Digite uma data no formato dd/mm/aaaa: ')

# processamento
def validarData(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# saída
if validarData(data):
    print('{} é uma data válida!'.format(data))
else:
    print('{} não é uma data válida!'.format(data))
