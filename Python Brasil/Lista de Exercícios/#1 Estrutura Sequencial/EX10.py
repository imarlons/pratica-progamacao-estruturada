# EXERCÍCIO 10

# faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# fórmula: (°F − 32) × 5/9 = -17,78 °C

# entrada
fahrenheit = int(input('Informe a temperatura da sua cidade em °F: '))

# processamento 
celsius = (fahrenheit - 32) * 5/9

# saída
print('A temperatura da sua cidade em Celsius é {:.2f}°'.format(celsius))