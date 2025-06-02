numero = 0
maiorNumero = 0

while (numero != -1):
    numero = int(input('informe um número: '))
    if (numero > maiorNumero):
        maiorNumero = numero

print('Dos números digitados, o maior deles é: {}'.format(maiorNumero))
    