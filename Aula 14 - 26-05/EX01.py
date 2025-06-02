nFatorar = int(input("quantos valores você deseja calcular o fatorial? "))
contador = 0
while (contador < nFatorar + 1):
    fatorar = int(input("informe um número para ver seu fatorial: "))
    fatorial = 1
    print(f'{fatorar}! = ', end='')
    contador = fatorar
    while (contador > 0):
        fatorial *= contador
        if contador == fatorar:
            print(contador, end='')
        else:
            print(f' X {contador}', end='')
        contador -= 1
    nFatorar -= 1
    print(f' = {fatorial}')
    contador += 1