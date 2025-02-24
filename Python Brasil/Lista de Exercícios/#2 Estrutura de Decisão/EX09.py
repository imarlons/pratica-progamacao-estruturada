# EXERCÍCIO 09

# faça um programa que leia três números e mostre-os em ordem decrescente.

# entrada de dados com for
numeros = []

for i in range(3):
    numero = int(input(f'Informe o {i+1}º número: '))
    numeros.append(numero)

# processamento
# ordenando em ordem decrescente
numeros.sort(reverse=True)

# saída
print('Números em ordem decrescente: {}'.format(numeros))
