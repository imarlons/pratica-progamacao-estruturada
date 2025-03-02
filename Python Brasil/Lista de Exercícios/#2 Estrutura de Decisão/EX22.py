# EXERCÍCIO 22

# faça um programa que peça um número inteiro e determine se ele é par ou impar. dica: utilize o operador módulo (resto da divisão).

# entrada
numero = int(input('Informe um número inteiro para saber se ele é Ímpar ou Par: '))

# processamento & saída
if (numero % 2 == 0):
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))