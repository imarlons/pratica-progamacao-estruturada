# EXERCÍCIO 26

# um posto está vendendo combustíveis com a seguinte tabela de descontos:
# álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

precoAlcool = 1.90
precoGasolina = 2.50

# entrada
litros = float(input('Quantos litros você deseja abastecer? '))
tipoCombustivel = input('Digite o tipo de combustível! (A - Álcool, G - Gasolina): ').upper()

# processamento
if (tipoCombustivel == 'A'):
    if (litros <= 20):
        desconto = 0.03
    else:
        desconto = 0.05 
    valor = litros * precoAlcool * (1 - desconto)

elif (tipoCombustivel == 'G'):
    if (litros <= 20):
        desconto = 0.04 
    else:
        desconto = 0.06
    valor = litros * precoGasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido!")
    exit()

# saída
print('O valor a ser pago é R${:.2f}'.format(valor))


