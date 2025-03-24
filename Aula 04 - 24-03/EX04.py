# EXERCÍCIO 04

# um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
# faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, 
# calcule e mostre a comissão e o salário final do funcionário.

def calcularComissao():
    salario = float(input('Informe o seu salário: R$'))
    vendas = float(input('Informe o montante das suas vendas: R$'))

    comissao = vendas * 0.04
    salarioFinal = salario + comissao

    print('Parabéns pelas vendas, você receberá:')
    print('Comissão: R${:.2f} \nSalário Final: R${:.2f}'.format(comissao, salarioFinal))

calcularComissao()
