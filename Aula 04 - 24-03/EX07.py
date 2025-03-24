# EXERCÍCIO 07

# faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário.

def calcularTabuada():
    numero = int(input('Você quer saber a tabuada de qual número?: '))
    x0 = numero * 0
    x1 = numero * 1
    x2 = numero * 2
    x3 = numero * 3
    x4 = numero * 4
    x5 = numero * 5
    x6 = numero * 6
    x7 = numero * 7
    x8 = numero * 8
    x9 = numero * 9
    x10 = numero * 10

    print('A tabuada de {} é:'.format(numero))
    print('{} x 0 = {}'.format(numero, x0))
    print('{} x 1 = {}'.format(numero, x1))
    print('{} x 2 = {}'.format(numero, x2))
    print('{} x 3 = {}'.format(numero, x3))
    print('{} x 4 = {}'.format(numero, x4))
    print('{} x 5 = {}'.format(numero, x5))
    print('{} x 6 = {}'.format(numero, x6))
    print('{} x 7 = {}'.format(numero, x7))
    print('{} x 8 = {}'.format(numero, x8))
    print('{} x 9 = {}'.format(numero, x9))
    print('{} x 10 = {}'.format(numero, x10))

calcularTabuada()