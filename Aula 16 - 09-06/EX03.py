continuar = True
alturas = []

while continuar:
    altura = float(input('informe sua altura: ') )

if (altura == 0):
    continuar = False
else:
    alturas.append(altura)

alturas.sort()
print('A lista de altura é: {}'.format(alturas))
print('A menor altura é: {}'.format(alturas[0]))
print('A maior altura é: {}'.format(alturas[-1]))