# EXERCÍCIO 04

# faça um programa que peça as 4 notas bimestrais e mostre a média.

# entrada
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))

# processamento
notas = nota1 + nota2 + nota3 + nota4
media = notas / 4

# saída
print('A média do aluno é {}'.format(media))