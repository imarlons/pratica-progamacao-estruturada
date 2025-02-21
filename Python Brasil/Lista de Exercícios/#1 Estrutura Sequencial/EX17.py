# EXERCÍCIO 17

# faça um Programa para uma loja de tintas. o programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# entrada
area = float(input("Informe o tamanho da área a ser pintada em m²: "))

# acrescenta 10% de folga
areaComFolga = area * 1.1  

# cálculo da quantidade de tinta necessária
litrosNecessarios = areaComFolga / 6  

# opção 1: apenas latas de 18 litros
latas = math.ceil(litrosNecessarios / 18)
precoLatas = latas * 80

# opção 2: Apenas galões de 3,6 litros
galoes = math.ceil(litrosNecessarios / 3.6)
precoGaloes = galoes * 25

# opção 3: mistura de latas e galões para minimizar desperdício
latasMistura = litrosNecessarios // 18  # quantidade inteira de latas
resto = litrosNecessarios % 18  # quantidade que sobra
galoesMistura = math.ceil(resto / 3.6)
precoMistura = (latasMistura * 80) + (galoesMistura * 25)

# saída
print('\nOPÇÃO 1: APENAS LATAS DE 18L')
print('Quantidade de latas: {}'.format(latas))
print('Preço total: R${:.2f}'.format(precoLatas))

print('\nOPÇÃO 2: APENAS GALÕES DE 3.6L')
print('Quantidade de galões: {}'.format(galoes))
print('Preço total: R${:.2f}'.format(precoGaloes))

print('\nOPÇÃO 3: MISTURA DE LATAS E GALÕES PARA MINIMIZAR O DESPERDÍCIO')
print('Quantidade de latas: {}'.format(int(latasMistura)))
print('Quantidade de galões: {}'.format(galoesMistura))
print('Preço total: R${:.2f}'.format(precoMistura))
