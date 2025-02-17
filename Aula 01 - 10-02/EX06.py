# EXERCÍCIO 06

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = '--------------------'
# entrada
pesoRefeicao = float(input('Informe o peso da refeição: '))
print(linha)

# processamento
precoKg = 12 #O restaurante cobra R$12/kg
valorCobranca =  pesoRefeicao * precoKg

# saída
print('Valor a pagar: R${:.2f}'.format(valorCobranca))
print(linha)