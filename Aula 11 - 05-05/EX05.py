somaPar = 0
somaImpar = 0
somaMultiplos = 0

paramsInicial = int(input('Informe o parâmetro inicial: '))
paramsFinal = int(input('Informe o parâmetro final: '))
multiplo = int(input('Você deseja ver dos múltiplos de qual número? '))

if (paramsInicial < paramsFinal):
    for i in range(paramsInicial, paramsFinal + 1):
        if (i % 2 == 0):
            somaPar += i
        else:
            somaImpar += i
        if (i % multiplo == 0):
            somaMultiplos += i

    print(somaImpar)
    print(somaPar)
    print(somaMultiplos)

else:
 print('O parâmetro inical deve ser menor do que o parâmetro final!')
