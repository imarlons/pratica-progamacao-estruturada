tabuada = int(input('Informa a tabuada desejada: '))

for i in range(1, 11):
    resultado = i * tabuada
    print(' {} x {} = {}'.format(i, tabuada, resultado))