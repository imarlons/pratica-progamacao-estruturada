# EXERCÍCIO 13

# faça um programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# entrada
numero = int(input('Digite um número para exibir o dia da semana: '))

# procesassamento & saída
semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

if (numero > 0 and numero <= 7):
    dia = numero-1
    print(semana[dia])
else:
    print('Valor inválido!')