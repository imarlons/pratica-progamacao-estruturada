tabuada = int(input('Informa a tabuada desejada: '))
paramsInicial = int(input('Informe o parâmetro inicial: '))
paramsFinal = int(input('Informe o parâmetro final: '))

for i in range(paramsInicial, paramsFinal + 1):
    resultado = i * tabuada
    print(' {} x {} = {}'.format(i, tabuada, resultado))