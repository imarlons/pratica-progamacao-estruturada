# EXERCÍCIO 02

# faça um algoritmo que leia um número inteiro e mostre:
# ● mensagem indicando se este número é par ou ímpar
# ● mensagem indicando se este número é positivo ou negativo.

numero = int(input('Informe um número inteiro: '))

if (numero % 2 == 0):
    print('O número {} é PAR!'.format(numero))
    if (numero > 0):
        print('O número {} é POSITIVO!'.format(numero))
    else:
         print('O número {} é NEGATIVO!'.format(numero))
else:
    print('O número {} é ÍMPAR!'.format(numero))
    if (numero > 0):
        print('O número {} é POSITIVO!'.format(numero))
    else:
         print('O número {} é NEGATIVO!'.format(numero))