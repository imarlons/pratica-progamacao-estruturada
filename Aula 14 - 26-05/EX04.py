juca = 1.1
chico = 1.5
anos = 0

while(juca < chico):
    juca += 0.3
    chico += 0.2
    anos += 1

print('Juca precisa de {} anos para ser maior que o Chico Moedas'.format(anos))
print('Juca: {:.2f}m; \nChico: {:.2f}m;'.format(juca, chico))