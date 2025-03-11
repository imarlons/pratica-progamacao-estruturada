# EXERCÍCIO 07

# a fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: 
# lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
# se um comerciante compra uma determinada quantidade de cada formato, 
# faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

# entrada
lata = int(input('Quantas latas de 350ml você deseja comprar? '))
garrafinha = int(input('Quantas garrafas de 650ml você deseja comprar? '))
garrafa = int(input('Quantas garrafas de 2l você deseja comprar? '))

# processamento
litrosTotal = lata * 350 + garrafinha * 650 + garrafa * 2000

# saída
if (litrosTotal > 1000):
    print('O comerciante comprou {} litros de refrigerante!'.format(litrosTotal / 1000))
else:
    print('O comerciante comprou {}ml de refrigerante!'.format(litrosTotal))
