# EXERCÍCIO 28

# o Hipermercado Tabajara está com uma promoção de carnes que é imperdível. confira:

#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

# entrada
tipoCarne = input('Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ').strip().lower()
quantidade = float(input('Digite a quantidade de carne (Kg): '))

# processamento
if tipoCarne == 'file duplo':
    if quantidade <= 5:
        precoKg = 4.90
    else:
        precoKg = 5.80
elif tipoCarne == 'alcatra':
    if quantidade <= 5:
        precoKg = 5.90
    else:
        precoKg = 6.80
elif tipoCarne == 'picanha':
    if quantidade <= 5:
        precoKg = 6.90
    else:
        precoKg = 7.80
else:
    print('Tipo de carne inválido!')
    exit()

precoTotal = quantidade * precoKg

# pergunta sobre o tipo de pagamento
pagamento = input('O pagamento será no cartão Tabajara? (sim/não): ').strip().lower()

# verificação e cálculo do desconto, se aplicável
if pagamento == 'sim':
    desconto = precoTotal * 0.05
    valorFinal = precoTotal - desconto
    tipoPagamento = 'Cartão Tabajara'
else:
    desconto = 0
    valorFinal = precoTotal
    tipoPagamento = 'Outro pagamento'

# saída
print('\n--- CUPOM FISCAL ---')
print('Tipo de carne: {}'.format(tipoCarne.title()))
print('Quantidade: {:.2f}Kg'.format(quantidade))
print('Preço total: R${:.2f}'.format(precoTotal))
print('Tipo de pagamento: {}'.format(tipoPagamento))
print('Desconto: R$ {:.2f}'.format(desconto))
print('Valor a pagar: R$ {:.2f}'.format(valorFinal))

