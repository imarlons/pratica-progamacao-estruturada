# EXERCÍCIO 20

# faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# a mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# a mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# a mensagem "Aprovado com Distinção", se a média for igual a 10.

# entrada
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

# processamento & saída
media = (nota1 + nota2 + nota3) / 3

if (media >= 7  and media < 9.9):
    print('\nA média do aluno(a) é {}'.format(media))
    print('Aluno(a) está aprovado!')

elif (media < 7):
    print('\nA média do aluno(a) é {}'.format(media))
    print('Aluno(a) está reprovado!')

elif (media == 10):
    print('\nA média do aluno(a) é {}'.format(media))
    print('Aluno(a) está aprovado com distinção!')

else:
    print('\nValor inválido! Por favor, informe as notas corretamente!')