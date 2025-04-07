# EXERCÍCIO 02

# elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
# "São múltiplos" ou "Não são múltiplos"

valorA = int(input('Informe o primeiro valor inteiro: '))
valorB = int(input('Informe o segundo valor inteiro: '))

if (valorA % valorB == 0 or valorB % valorA == 0):
    print('Os números {} e {} são múltiplos!'.format(valorA, valorB))
else:
    print('Os números {} e {} não são múltiplos!'.format(valorA, valorB))