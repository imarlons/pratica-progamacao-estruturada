# EXERCÍCIO 03f=

# faça um algoritmo que receba o preço de um produto, 
# calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

def calcularDesconto():
    preco = float(input('Informe o preço do produto: R$'))
    
    desconto = preco * 0.10
    novoPreco = preco - desconto
    
    print('O novo preço com 10% de desconto é: R${:.2f}'.format(novoPreco))

calcularDesconto()