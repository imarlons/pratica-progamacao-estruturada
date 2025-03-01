# EXERCÍCIO 14

# faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# a atribuição de conceitos obedece à tabela abaixo:

#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0            A
#   Entre 7.5 e 9.0             B
#   Entre 6.0 e 7.5             C
#   Entre 4.0 e 6.0             D
#   Entre 4.0 e zero            E

# o algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E

# entrada
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

# processamento & saída
media = (nota1 + nota2) / 2

if (media > 9  and media <= 10):
    print('\nO média do aluno(a) é {} com as notas {} e {}'.format(media, nota1, nota2))
    print('O aluno é "CONCEITO A" e está "APROVADO"!')

elif (media > 7.5 and media <= 9):
    print('\nO média do aluno(a) é {} com as notas {} e {}'.format(media, nota1, nota2))
    print('O aluno é "CONCEITO B" e está "APROVADO"!')

elif (media > 6 and media <= 7.5):
    print('\nO média do aluno(a) é {} com as notas {} e {}'.format(media, nota1, nota2))
    print('O aluno é "CONCEITO C" e está "APROVADO"!')

elif (media > 4 and media <= 6):
    print('\nO média do aluno(a) é {} com as notas {} e {}'.format(media, nota1, nota2))
    print('O aluno é "CONCEITO D" e está "REPROVADO"!')

elif (media > 0 and media <= 4):
    print('\nO média do aluno(a) é {} com as notas {} e {}'.format(media, nota1, nota2))
    print('O aluno é "CONCEITO E" e está "REPROVADO"!')

else:
    print('\nValor inválido! Por favor, informe as notas corretamente!')