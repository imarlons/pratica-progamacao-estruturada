# EXERCÍCIO 02

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = '--------------------'
# entrada
primeiroValor = float(input('Infome o primeiro valor: ')) # o tipo da informação foi definido como float, caso algum número decimal seja informado
segundoValor = float(input('Infome o segundo valor: '))

# processamento
soma = primeiroValor + segundoValor
subtracao = primeiroValor  - segundoValor
multiplicacao = primeiroValor * segundoValor
divisao = primeiroValor / segundoValor
print(linha)

# saída
print('Os valores informados foram {:.2f} e {:.2f}.'.format(primeiroValor, segundoValor))
print(linha)
print('O sistema processou os valores com sucesso!')
print('Os resultados das operações são: \nSoma = {:.2f} \nSubtração = {:.2f} \nMultiplicação = {:.2f} \nDivisão = {:.2f}'.format(soma, subtracao, multiplicacao, divisao))
print(linha)