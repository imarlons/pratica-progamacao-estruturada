valorFatorar = int(input('Informe um valor: '))
resultado = 1
extensao = ''


for i in range(1, valorFatorar + 1):
    resultado = resultado * i
    extensao  += str(i)
    if (i >= 1 and i < valorFatorar):
        extensao += 'x'

print('{}! = {} = {}'.format(valorFatorar, extensao, resultado))




