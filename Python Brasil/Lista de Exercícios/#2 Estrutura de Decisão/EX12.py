# EXERCÍCIO 12

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). o salário líquido corresponde ao salário bruto menos os descontos. 
# o programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 

# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220): R$ 1100,00
# (-) IR (5%)             : R$   55,00  
# (-) INSS ( 10%)         : R$  110,00
# FGTS (11%)              : R$  121,00
# Total de descontos      : R$  165,00
# Salário Liquido         : R$  935,00

# entrada
ganhoPorHora = float(input('Informe quanto você ganha por hora: R$'))
horasMes = float(input('Informe quantas horas você trabalhou neste mês: '))

# processamento & saída
salario = ganhoPorHora * horasMes

if (salario > 0 and salario <= 900):
    inss = salario * 0.1
    fgts = salario * 0.11
    sindicato = salario * 0.03
    descontos = inss + sindicato
    salarioLiquido = salario - descontos

    print('\nSalário Bruto (R${:.2f} * {:.2f} horas): R${:.2f}'.format(ganhoPorHora, horasMes, salario))
    print('(-) IR                               : Você é insento!')
    print('(-) INSS (10%)                       : R${:.2f}'.format(inss))
    print('(-) Sindicato (3%)                   : R${:.2f}'.format(sindicato))
    print('FGTS (11%)                           : R${:.2f}'.format(fgts))
    print('Total de Descontos                   : R${:.2f}'.format(descontos))
    print('Salário Líquido                      : R${:.2f}'.format(salarioLiquido))

elif (salario > 900 and salario <= 1500):
    impostoDeRenda = salario * 0.05
    inss = salario * 0.1
    fgts = salario * 0.11
    sindicato = salario * 0.03
    descontos = inss + impostoDeRenda + sindicato
    salarioLiquido = salario - descontos

    print('\nSalário Bruto (R${:.2f} * {:.2f} horas): R${:.2f}'.format(ganhoPorHora, horasMes, salario))
    print('(-) IR (5%)                           : R${:.2f}'.format(impostoDeRenda))
    print('(-) INSS (10%)                        : R${:.2f}'.format(inss))
    print('(-) Sindicato (3%)                    : R${:.2f}'.format(sindicato))
    print('FGTS (11%)                            : R${:.2f}'.format(fgts))
    print('Total de Descontos                    : R${:.2f}'.format(descontos))
    print('Salário Líquido                       : R${:.2f}'.format(salarioLiquido))

elif (salario > 1500 and salario <= 2500):
    impostoDeRenda = salario * 0.1
    inss = salario * 0.1
    fgts = salario * 0.11
    sindicato = salario * 0.03
    descontos = inss + impostoDeRenda + sindicato
    salarioLiquido = salario - descontos

    print('\nSalário Bruto (R${:.2f} * {:.2f} horas): R${:.2f}'.format(ganhoPorHora, horasMes, salario))
    print('(-) IR (10%)                          : R${:.2f}'.format(impostoDeRenda))
    print('(-) INSS (10%)                        : R${:.2f}'.format(inss))
    print('(-) Sindicato (3%)                    : R${:.2f}'.format(sindicato))
    print('FGTS (11%)                            : R${:.2f}'.format(fgts))
    print('Total de Descontos                    : R${:.2f}'.format(descontos))
    print('Salário Líquido                       : R${:.2f}'.format(salarioLiquido))

elif (salario > 2500):
    impostoDeRenda = salario * 0.2
    inss = salario * 0.1
    fgts = salario * 0.11
    sindicato = salario * 0.03
    descontos = inss + impostoDeRenda + sindicato
    salarioLiquido = salario - descontos

    print('\nSalário Bruto (R${:.2f} * {:.2f} horas): R${:.2f}'.format(ganhoPorHora, horasMes, salario))
    print('(-) IR (20%)                          : R${:.2f}'.format(impostoDeRenda))
    print('(-) INSS (10%)                        : R${:.2f}'.format(inss))
    print('(-) Sindicato (3%)                    : R${:.2f}'.format(sindicato))
    print('FGTS (11%)                            : R${:.2f}'.format(fgts))
    print('Total de Descontos                    : R${:.2f}'.format(descontos))
    print('Salário Líquido                       : R${:.2f}'.format(salarioLiquido))

else:
    print('Valor inválido! Por favor, informe o seu salário corretamente!')
