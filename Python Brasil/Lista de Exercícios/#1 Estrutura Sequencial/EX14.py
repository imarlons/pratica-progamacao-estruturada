# EXERCÍCIO 14

# João papo-de-pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de SP (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

# entrada
peso = float(input('João, quantos quilos de peixe você pescou hoje? '))

# processamento & saída
if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print('João pescou {:.2f}kg e excedeu o limite por {:.2f}kg, logo, terá que pagar uma multa de R${:.2f}'.format(peso, excesso, multa))
else:
    print('João pescou {:.2f}kg e não passou do limite, logo, não haverá multa!'.format(peso))