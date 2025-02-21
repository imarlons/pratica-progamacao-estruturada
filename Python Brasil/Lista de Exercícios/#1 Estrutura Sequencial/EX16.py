# EXERCÍCIO 16

# faça um programa para uma loja de tintas. o programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

# entrada
area = float(input('Informe o tamanho da área a ser pintada em m²: '))

# processamento
litros = area / 3
quantidadeDeLatas = math.ceil(litros / 18)  # arredonda para cima
precoTotal = quantidadeDeLatas * 80 

# saída
print('Você precisará de {} lata(s) de tinta e isso custará R${}'.format(quantidadeDeLatas, precoTotal))
