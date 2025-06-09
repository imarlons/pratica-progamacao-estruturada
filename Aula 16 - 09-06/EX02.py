contador = 0
numeros = []

for i in range(0,5):
    valor = int(input(f'informe o {i + 1}º valor: '))
    numeros.append(valor)

for num in numeros:
    if (num % 2 == 0):
        contador += 1

print('na lista {} há {} números par(es)'.format(numeros, contador))