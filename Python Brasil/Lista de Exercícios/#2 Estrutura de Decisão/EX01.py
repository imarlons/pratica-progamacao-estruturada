# EXERCÍCIO 01

# faça um Programa que peça dois números e imprima o maior deles.

# entrada
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

# processamento & saída
if (numero1 > numero2):
    print('O maior número é {}'.format(numero1))
elif (numero2 > numero1):
    print('O maior número é {}'.format(numero2))
else:
    print('Os dois números são iguais!')

