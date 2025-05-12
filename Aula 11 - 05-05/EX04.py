somaPar = 0
somaImpar = 0
somaMultiplosDeTres = 0

paramsInicial = int(input('Informe o parâmetro inicial: '))
paramsFinal = int(input('Informe o parâmetro final: '))

if (paramsInicial < paramsFinal):
    for i in range(paramsInicial, paramsFinal + 1):
        if (i % 2 == 0):
            somaPar += i
        else:
            somaImpar += i
        if (i % 3 == 0):
            somaMultiplosDeTres += i

    print(somaImpar)
    print(somaPar)
    print(somaMultiplosDeTres)
    print(paramsFinal)

else:
 print('O parâmetro inical deve ser menor do que o parâmetro final!')
