# EXERCÍCIO 15

# faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + salário bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - sindicato ( 5%) : R$
# = salário Liquido : R$
# obs.: salário bruto - descontos = salário líquido.

# entrada
ganhoPorHora = float(input('Informe quanto você ganha por hora: R$'))
horasMes = float(input('Informe quantas horas você trabalhou neste mês: '))

# processamento
salarioBruto = ganhoPorHora * horasMes
impostoDeRenda =  salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
impostos = impostoDeRenda + inss + sindicato
salarioLiquido = salarioBruto - impostos

# saída
print('O seu salário bruto é R${:.2f}'.format(salarioBruto))
print('O impostos equivalem a \nIR (11%): R${:.2f} \nINSS (8%): R${:.2f} \nSindicato (5%): R${:.2f}'.format(impostoDeRenda, inss, sindicato))
print('O seu salário líquido será R${:.2f}'.format(salarioLiquido))

