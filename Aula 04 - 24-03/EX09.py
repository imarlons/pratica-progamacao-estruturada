# EXERCÍCIO 09

# joão recebeu seu salário de R$1200,00 e precisa pagar duas contas (C1 =R$200,00 e C2 = R$120,00) que estão atrasadas. 
# como as contas estão atrasadas, joão terá de pagar multa de 2% sobre cada conta. 
# faça um algoritmo que calcule e mostre quanto restará do salário do joão.

def calcularRestoSalario():
    salario = 1200
    c1 = 200
    c2 = 120
    multa = 0.02

    restoSalario = salario - ((c1 + (c1 * multa)) + (c2 + (c2 * multa)))

    print('Após pagar as contas atrasadas, João terá R${:.2f} restante do seu salário.'.format(restoSalario))

calcularRestoSalario()