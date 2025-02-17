# faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# fórmula: (A = π r²) 
# π = 3.14

# entrada
raio = float(input('Informe o raio do círculo: '))

# processamento
area = 3.14 * (raio ** raio)

# saída
print('A área do círculo é {}'.format(area))