# EXERCÍCIO 16

# faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# o programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

# entrada
def calcularRaizes():
    # Solicita os coeficientes ao usuário
    a = float(input('Informe o valor de A: '))
    
    # verifica se a equação é realmente do segundo grau
    if a == 0:
        print('A equação não é do segundo grau. Encerrando o programa...')
        return
    
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    
    # processamento & saída
    # calcula o delta
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print('A equação não possui raízes reais.')

    elif delta == 0:
        x = -b / (2 * a)
        print('A equação possui apenas uma raiz real: x = {:.2f}'.format(x))

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('A equação possui duas raízes reais: x1 = {:.2f} e x2 = {:.2f}'.format(x1, x2))

calcularRaizes()
