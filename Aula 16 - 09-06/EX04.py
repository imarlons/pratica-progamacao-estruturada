lista = []
tamanho = int (input('informe o tamanho da lista: '))

for item in range(0, tamanho):
    valor = int(input('informe um valor: '))
    lista.append(valor)

print(lista)

for i in range(0, len(lista)):
    if (lista[i] < 0):
        lista[i] = 0

print(lista)