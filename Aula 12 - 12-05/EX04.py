tabuada = int(input('Informa a tabuada desejada: '))
contador = 1

# for i in range(1, 11):
#     resultado = i * tabuada
#     print(' {} x {} = {}'.format(i, tabuada, resultado))

while (contador <= 10):
    resultado = tabuada * contador
    print(' {} x {} = {}'.format(tabuada, contador, resultado))

    contador += 1

