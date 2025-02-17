# EXERCÍCIO 03

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = '--------------------'
# entrada
numeroDeCavalos = int(input('Informe a quantidade de cavalos que você possui no seu haras: '))
print(linha)

# processamento
calculo = numeroDeCavalos * 4
numeroDeFerraduras = calculo

# saída
print('Você possui {} cavalos no seu haras. Logo, você precisará comprar {} ferraduras para realizar o cuidado de todos eles.'.format(numeroDeCavalos, numeroDeFerraduras))
print(linha)
