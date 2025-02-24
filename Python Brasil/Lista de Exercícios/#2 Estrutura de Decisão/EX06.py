# EXERCÍCIO 06

# faça um programa que leia três números e mostre o maior deles.

# entrada
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

# processamento & saída
if (numero1 > numero2 and numero1 > numero3):
    print('O maior número é {}'.format(numero1))
elif (numero2 > numero1 and numero2 > numero3):
    print('O maior número é {}'.format(numero2))
elif (numero3 > numero1 and numero3 > numero2):
    print('O maior número é {}'.format(numero3))
else:
    print('Os números são iguais!')

