limiteInferior = int(input('Digite o limite inferior: '))
limiteSuperior = int(input('Digite o limite superior: '))

somaPares = 0

print('\nNúmeros pares no intervalo aberto ({} - {}):'.format(limiteInferior, limiteSuperior))
for numero in range(limiteInferior + 1, limiteSuperior):
    if (numero % 2 == 0):
        print(numero, end=' ')
        somaPares += numero

print('\nSoma dos números pares: {}'.format(somaPares))
