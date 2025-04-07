# EXERCÍCIO 01

# escrever um algoritmo que lê 
# o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios 
# que fazem parte da avaliação. 
# calcular a média de aproveitamento, usando a fórmula:

# MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME ) / 7

# a atribuição de conceitos obedece a tabela abaixo:

# Média de Aproveitamento  Conceito
# 9,0                         A
# 7,5 e < 9,0                 B
# 6,0 e < 7,5                 C
# 4,0 e < 6,0                 D
# < 4,0                       E

# o algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, 
# o conceito correspondente e a mensagem: APROVADO se o conceito for A,B ou C e REPROVADO se o conceito for D ou E.


idAluno = int(input('Informe o número de identificação do aluno: '))

notas = []

for i in range(3):
    nota = float(input('Informe a {}ª nota do aluno: '.format(i+1)))
    notas.append(nota)

mediaEx = float(input('Informe a média dos exercícios do aluno: '))

mediaAprov = (notas[0] + notas[1] * 2 + notas[2] * 3 + mediaEx) / 7

if (mediaAprov >= 9):
    conceito = 'A'
    resultado = 'APROVADO'
elif (mediaAprov >= 7.5 and mediaAprov < 9):
    conceito = 'B'
    resultado = 'APROVADO'
elif (mediaAprov >= 6 and mediaAprov < 7.5):
    conceito = 'C'
    resultado = 'APROVADO'
elif (mediaAprov >= 4 and mediaAprov < 6):
    conceito = 'D'
    resultado = 'REPROVADO'
elif (mediaAprov >= 0 and mediaAprov < 4):
    conceito = 'E'
    resultado = 'REPROVADO'

if (mediaAprov != 0):
    print('\nID do Aluno: {}'.format(idAluno))
    print('Notas do Aluno: {}'.format(notas))
    print('Média do Exercícios: {}'.format(mediaEx))
    print('Média de Aproveitamento: {:.1f}'.format(mediaAprov))
    print('Conceito do Aluno: {}'.format(conceito))
    print('Situação do Aluno: {}'.format(resultado))
else:
    print('Valores inválidos! Insira as informações corretamente!')


