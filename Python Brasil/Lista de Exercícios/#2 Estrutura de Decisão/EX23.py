# EXERCÍCIO 23

# faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# fica: utilize uma função de arredondamento.

def verificarNumero(numero):
    if numero == round(numero):
        print('O número {} é inteiro!'.format(numero))
    else:
        print('O número {} é decimal!'.format(numero))

# entrada
try:
    num = float(input('Informe um número: '))
    verificarNumero(num)
except ValueError:
    print('Valor inválido! Por favor, digite um número corretamente!')
