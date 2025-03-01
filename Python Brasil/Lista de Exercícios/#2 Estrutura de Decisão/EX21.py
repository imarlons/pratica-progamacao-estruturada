# EXERCÍCIO 21

# faça um programa para um caixa eletrônico. 
# o programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# as notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# o valor mínimo é de 10 reais e o máximo de 600 reais. 
# o programa não deve se preocupar com a quantidade de notas existentes na máquina.

def caixaEletronico():
    print("----- CAIXA ELETRÔNICO -----")

    # entrada
    valor = int(input('Digite o valor do saque (mínimo R$10 e máximo R$600): R$'))

    # processamento
    if valor < 10 or valor > 600:
        print('Valor inválido! O saque deve estar entre R$10 e R$600.')
        return
    
    notas = [100, 50, 10, 5, 1] # notas disponíveis

    distribuicao = {} # para armazenar a quantidade de cada nota

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            distribuicao[nota] = quantidade
            valor -= quantidade * nota

    # saída
    print("\nNOTAS FORNECIDAS:")
    for nota, quantidade in distribuicao.items():
        print('Para sacar a quantia de R${}, você receberá {} nota(s) de R${}'.format(nota * quantidade, quantidade, nota))

# chama a função e executa o programa
caixaEletronico()