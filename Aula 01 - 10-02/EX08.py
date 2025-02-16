# EXERCÍCIO 08

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = ('--------------------')
# entrada
salarioInicial = float(input('Informe o seu salário: '))

# processamento
aumento = 0.15 #o aumento vale 15%
salarioNovo = (salarioInicial * aumento) + salarioInicial
imposto = 0.08 # o imposto vale 8%
salarioFinal = salarioNovo - (salarioNovo * 0.08)  
print(linha)

# saída
print('O salário atual é R${:.2f} \nO salário com aumento será R${:.2f} \nMASSS como a vida não é doce e temos impostos... \nO salário final será R${:.2f}'.format(salarioInicial, salarioNovo, salarioFinal))
print(linha)