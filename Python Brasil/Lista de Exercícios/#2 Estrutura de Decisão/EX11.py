# EXERCÍCIO 11

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.
# faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

# entrada
salarioAtual = float(input('Informe o seu salário: R$'))

# processamento & saída
if (salarioAtual > 0 and salarioAtual <= 280):
    aumento = salarioAtual * 0.2 # aumento de 20%
    salarioNovo = salarioAtual * 1.2
    percentual = 20
    
    print('O seu salário antes do reajuste era R${:.2f}'.format(salarioAtual))
    print('O percentual aplicado foi de {}%, resultando em um aumento de R${:.2f}'.format(percentual, aumento))
    print('O seu novo salário será R${:.2f}'.format(salarioNovo))

elif (salarioAtual > 280 and salarioAtual <= 700):
    aumento = salarioAtual * 0.15 # aumento de 15%
    salarioNovo = salarioAtual * 1.15
    percentual = 15

    print('O seu salário antes do reajuste era R${:.2f}'.format(salarioAtual))
    print('O percentual aplicado foi de {}%, resultando em um aumento de R${:.2f}'.format(percentual, aumento))
    print('O seu novo salário será R${:.2f}'.format(salarioNovo))

elif (salarioAtual > 700 and salarioAtual <= 1500):
    aumento = salarioAtual * 0.1 # aumento de 10%
    salarioNovo = salarioAtual * 1.10
    percentual = 10

    print('O seu salário antes do reajuste era R${:.2f}'.format(salarioAtual))
    print('O percentual aplicado foi de {}%, resultando em um aumento de R${:.2f}'.format(percentual, aumento))
    print('O seu novo salário será R${:.2f}'.format(salarioNovo))

elif (salarioAtual > 1500):
    aumento = salarioAtual * 0.05 # aumento de 5%
    salarioNovo = salarioAtual * 1.05
    percentual = 5

    print('O seu salário antes do reajuste era R${:.2f}'.format(salarioAtual))
    print('O percentual aplicado foi de {}%, resultando em um aumento de R${:.2f}'.format(percentual, aumento))
    print('O seu novo salário será R${:.2f}'.format(salarioNovo))

else:
    print('Valor inválido! Por favor, informe o seu salário corretamente!')