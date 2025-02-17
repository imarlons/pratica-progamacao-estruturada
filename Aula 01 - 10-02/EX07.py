# EXERCÍCIO 07

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = '--------------------'
# entrada
diaAtual = int(input('Considerando que o mês possui somente 30 dias. Informe o dia do mês: '))
mesAtual =  int(input('Considerando que Janeiro = 1, Fevereiro = 2... Informe o número do mês: '))
print(linha)

# processamento
diasPorMes = 30
diferencaDeDias = diasPorMes - diaAtual
quantidadeDias = (diasPorMes * mesAtual) - diferencaDeDias

# saída
print('Já se passaram {} dias desde o começo do ano!'.format(quantidadeDias))
print(linha)

    