# EXERCÍCIO 27

# uma fruteira está vendendo frutas com a seguinte tabela de preços

#                 Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# se o cliente comprar mais de 8Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# entrada
quantidadeDeMorango = float(input("Digite a quantidade de morangos (Kg): "))
quantidadeDeMaca = float(input("Digite a quantidade de maçãs (Kg): "))

# processamento
# definindo os preços por Kg para as duas faixas
if (quantidadeDeMorango <= 5):
    precoMorango = 2.50
else:
    precoMorango = 2.20

if (quantidadeDeMaca <= 5):
    precoMaca = 1.80
else:
    precoMaca = 1.50

# calculando o valor total sem desconto
valorMorango = quantidadeDeMorango * precoMorango
valorMaca = quantidadeDeMaca * precoMaca
valorTotal = valorMorango + valorMaca

# verificando se o cliente tem direito ao desconto
if (quantidadeDeMorango + quantidadeDeMaca > 8 or valorTotal > 25.00):
    valorTotal = valorTotal * 0.90  # aplicando 10% de desconto

# saída
print('O valor a ser pago pelo cliente é R${:.2f}'.format(valorTotal))
