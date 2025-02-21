# EXERCÍCIO 11

# faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

# os números reais são um conjunto que inclui todos os números positivos, negativos, decimais, 
# fracionários, zero, dízimas periódicas e não periódicas.

# entrada
numero1 = int(input('Informe o primeiro valor: '))
numero2 = int(input('Informe o segundo valor: '))
numero3 = float(input('Informe o terceiro valor: '))

# processamento
questaoA = (numero1 * 2) + (numero2 / 2)
questaoB = numero1 * 3 + numero3
questaoC = numero3 ** 3

# saída
print('O produto do dobro do primeiro com metade do segundo é {}'.format(questaoA))
print('A soma do triplo do primeiro com o terceiro é {}'.format(questaoB))
print('O produto do terceiro elevado ao cubo é {}'.format(questaoC))
