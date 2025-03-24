# EXERCÍCIO 01

# Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
# faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. 
# considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real.
# não havendo moeda de um tipo, a quantidade respectiva é zero.

def calcularEconomia():
    umCent = int(input('Informe a quantidade de moedas de 1 centavo (R$0,01): '))
    cincoCent = int(input('Informe a quantidade de moedas de 5 centavos (R$0,05): '))
    dezCent = int(input('Informe a quantidade de moedas de 10 centavos (R$0,10): '))
    vintCent = int(input('Informe a quantidade de moedas de 25 centavos (R$0,25): '))
    cinqCent = int(input('Informe a quantidade de moedas de 50 centavos (R$0,50): '))
    umReal = int(input('Informe a quantidade de moedas de 1 real (R$1,00): '))
    
    totalEconomia = (umCent * 0.01) + (cincoCent * 0.05) + (dezCent * 0.10) + (vintCent * 0.25) + (cinqCent * 0.50) + (umReal * 1.00)

    print('Pedrinho conseguiu econmizar R${:.2f}'.format(totalEconomia))

calcularEconomia()