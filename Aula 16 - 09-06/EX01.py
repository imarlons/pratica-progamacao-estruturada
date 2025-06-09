tamanhoLista = int(input ('Informe o tamanho da lista: '))

listaInicial = []

for i in range(0,tamanhoLista):
    valor = int(input(f'Informe o {i+1}º valor: '))
    listaInicial.append(valor)
    print(listaInicial)

listaInicial.reverse()

print('\n{}'.format(listaInicial))