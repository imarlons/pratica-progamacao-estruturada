# faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# calcule e mostre o total do seu salário no referido mês.

# entrada
ganhoPorHora = float(input('Quanto você ganha por hora? '))
horasMes = float(input('Quantas horas você trabalhou neste mês? '))

# processamento
salario = ganhoPorHora * horasMes

# saída
print('O seu salário será R${:.2f}'.format(salario))