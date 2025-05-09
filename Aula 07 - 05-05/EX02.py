somaPar = 0
somaImpar = 0
somaMultiplosDeTres = 0

for i in range(1, 500):
    if (i % 2 == 0):
        somaPar += i
    else:
        somaImpar += i
    if (i % 3 == 0):
        somaMultiplosDeTres += i

print(somaImpar)
print(somaPar)
print(somaMultiplosDeTres)
