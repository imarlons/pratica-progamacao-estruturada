# EXERCÍCIO 15

# faça um programa que peça os 3 lados de um triângulo. o programa deverá informar se os valores podem ser um triângulo. 
# indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 
# dicas:
# três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# para três valores A, B e C formarem um triângulo, eles precisam atender à desigualdade triangular:
# a + b > c, 
# a + c > b,
# b + c > a
# se essas três condições forem verdadeiras, os valores formam um triângulo. caso contrário, não podem formar um triângulo.
# triângulo Equilátero: três lados iguais;
# triângulo Isósceles: quaisquer dois lados iguais;
# triângulo Escaleno: três lados diferentes;

# entrada
ladoA = float(input('Informe o tamanho do primeiro lado: '))
ladoB = float(input('Informe o tamanho do segundo lado: '))
ladoC = float(input('Informe o tamanho do terceiro lado: '))

# processamento & saída
if (ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA):
    print('\nOs valores formam um triângulo!')
    if (ladoA == ladoB == ladoC):
        print('O triângulo é equilátero, ou seja, possui três lados iguais!')
    
    elif (ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
        print('O triângulo é isósceles, ou seja, possui dois lados iguais!')

    else:
        print('O triângulo é escaleno, ou seja, possui três lados diferentes!')

else:
    print('Os valores não formam um triângulo!')