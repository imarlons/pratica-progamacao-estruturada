# EXERCÍCIO 05

#  faça um programa para a leitura de duas notas parciais de um aluno. 
# o programa deve calcular a média alcançada por aluno e apresentar:
# a mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# a mensagem "Reprovado", se a média for menor do que sete;
# a mensagem "Aprovado com Distinção", se a média for igual a dez.

# entrada
nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

# processamento
media = (nota1 + nota2) / 2

# saída
if (media >= 7 and media < 10):
    print('Aprovado!')
elif (media == 10):
    print('Aprovado com Distinção!')
else:
    print('Reprovado!')

