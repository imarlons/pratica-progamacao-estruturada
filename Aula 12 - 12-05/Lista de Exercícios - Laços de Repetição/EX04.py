total = 0

for a in range(1, 6):
    numero = int(input(f'Informe o {a}º número: '))
    if (numero < 0):
        total += 1
    
print('Total de números negativo: {}'.format(total))