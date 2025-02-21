# EXERCÍCIO 18

# faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

# entrada
tamanhoDoArquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidadeInternet = float(input('Informe a velocidade da internet em Mbps: '))

# processamento
tempoEmSegundos = (tamanhoDoArquivo * 8) / velocidadeInternet # conversão de megabytes para megabits
tempoEmMinutos = math.ceil(tempoEmSegundos / 60)

# saída
print('O download vai demorar aproximadamente {} minutos'.format(int(tempoEmMinutos)))