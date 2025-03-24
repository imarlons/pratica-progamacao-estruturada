# EXERCÍCIO 06

# faça um algoritmo que receba o valor do salário mínimo e o valor do salário de um funcionário, 
# calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

def calcularSalario():
    salarioMinimo = 1509
    salarioFuncionario = float(input('Informe o seu salário: R$'))

    quantidadeSalario = int(salarioFuncionario // salarioMinimo)

    if (quantidadeSalario >= 1):
        print('O seu salário tem a compatibilidade com aproximadamente {} salário minimo!'.format(quantidadeSalario))
    else:
        print('Que triste, você é estagiário!')

calcularSalario()

