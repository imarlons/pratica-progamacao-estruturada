somaNegativos = 0  
contador = 0

while (contador < 10):
    numero = int (input('informe um valor: '))
    if (numero < 0):
       somaNegativos += numero
    contador += 1
print ('o somatório dos números negativos é: {}'.format(somaNegativos))