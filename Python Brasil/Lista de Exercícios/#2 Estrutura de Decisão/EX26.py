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

# valor dos combustíveis disponíveis para venda
precoAlcool = 1.90
precoGasolina = 2.50

# entrada 
# entrada de informações, aqui o usuário informará a quantiade de litros que ele deseja e o tipo de combustível
litros = float(input('Quantos litros você deseja abastecer? '))
tipoCombustivel = input('Digite o tipo de combustível! (A - Álcool, G - Gasolina): ').upper()

# processamento
# processamento de informações, aqui o sistema vai verificar o tipo de combustível e a quantiadade de combustível que será abastecido
if (tipoCombustivel == 'A'): # se o combustível escolhido for A (Álcool), o programa entrará nesse bloco de execução.
    if (litros <= 20): # se a quantidade de combustível abastecido for igual ou menor a 20 litros, o sistema aplicará uma quantidade X de desconto
        desconto = 0.03
    else: # se for maior, ele aplicará outro valor de desconto.
        desconto = 0.05 
    valor = litros * precoAlcool * (1 - desconto)  # se o desconto for 3% → 1 - 0.03 = 0.97 | se for 5% → 1 - 0.05 = 0.95

elif (tipoCombustivel == 'G'): # se o combustível escolhido for G (Gasolina), o programa entrará nesse bloco de execução.
    if (litros <= 20): # se a quantidade de combustível abastecido for igual ou menor a 20 litros, o sistema aplicará uma quantidade X de desconto
        desconto = 0.04 
    else: # se for maior, ele aplicará outro valor de desconto.
        desconto = 0.06
    valor = litros * precoGasolina * (1 - desconto) # se o desconto for 4% → 1 - 0.04 = 0.96 | se for 6% → 1 - 0.06 = 0.94

else: # se o tipo de combustível não for A ou G, o programa executará esse bloco de execução e finalizará o programa.
    print("Tipo de combustível inválido!")
    exit()

# saída
# se tudo tiver ocorrido bem e ter sido bem informado e executado, o programa vai retornar o valor que o cliente tem que pagar.
print('O valor a ser pago é R${:.2f}'.format(valor))


