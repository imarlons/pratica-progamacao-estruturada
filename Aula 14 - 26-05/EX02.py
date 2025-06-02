nValor = int(input('quantos valores serão lidos? '))
contador = 0

cont0a25 = 0
cont26a50 = 0
cont51a75 = 0
cont76a100 = 0

while (contador < nValor):
    valor = int(input('informe um número para ser lido: '))
    if (valor > 0 and valor <= 25):
        cont0a25 += 1
    elif (valor > 25 and valor <= 50):
        cont26a50 += 1
    elif (valor > 50 and valor <= 75):
        cont51a75 += 1
    elif (valor > 75 and valor <= 100):
        cont76a100 += 1
    contador +=1

print('{} número(s) no intevalo de 0 a 25'.format(cont0a25))
print('{} número(s) no intevalo de 26 a 50'.format(cont26a50))
print('{} número(s) no intevalo de 51 a 75'.format(cont51a75))
print('{} número(s) no intevalo de 76 a 100'.format(cont76a100))

