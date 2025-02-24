# EXERCÍCIO 08

# faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

# entrada
produtos = []

for i in range(3):
    produto = int(input(f'Informe o valor do {i+1}º produto: R$'))
    produtos.append(produto)

# processamento
maior = menor = produtos[0]
for escolha in produtos[1:]:
    if (escolha < menor):
        menor = escolha

# saída
if len(set(produtos)) == 1:
    print('Os valores são iguais!')
else:
    print('Você deve comprar o produto que custa R${}'.format(menor))

