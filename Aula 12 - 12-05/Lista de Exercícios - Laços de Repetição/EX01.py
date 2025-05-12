alturas = []

for i in range(15):
    while True:
        try:
            altura = float(input(f'Informe a {i+1}ª altura em metros: '))
            if altura > 0:
                alturas.append(altura)
                break
            else:
                print('Por favor, digite uma altura válida, maior que zero.')
        except ValueError:
            print('Entrada inválida. Digite um número válido!') 

menorAlt= min(alturas)
maiorAlt = max(alturas)

print('A menor altura do grupo: {:.2f} m'.format(menorAlt))
print('A maior altura do grupo: {:.2f} m'.format(maiorAlt))