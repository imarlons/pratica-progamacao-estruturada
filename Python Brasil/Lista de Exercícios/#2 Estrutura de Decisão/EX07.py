# EXERCÍCIO 07

# faça um programa que leia três números e mostre o maior e o menor deles.

# entrada
numeros = []

for i in range(3):
    numero = int(input(f'Informe o {i+1}º número: '))
    numeros.append(numero)

# processamento
maior = menor = numeros[0]
for num in numeros[1:]:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# saída
if len(set(numeros)) == 1:
    print('Os números são iguais!')
else:
    print(f'O maior número é {maior}')
    print(f'O menor número é {menor}')
