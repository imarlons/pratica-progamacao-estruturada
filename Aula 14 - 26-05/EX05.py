contador100a200 = 0
numero = 1
contador = 0

while (numero != 0):
    numero = int(input('informe um número: '))
    contador += 1
    if (numero >= 100 and numero <= 200):
        contador100a200 += 1
    
print('Dos {} números digitados, {} estão entre 100 e 200.'.format(contador, contador100a200))