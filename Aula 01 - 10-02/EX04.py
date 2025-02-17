# EXERCÍCIO 04

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = '--------------------'
# entrada
quantidadeDePao = int(input('Quantos pães foram vendidos hoje? '))
quantidadeDeBroa = int(input('Quantas broas foram vendidas hoje? '))

# processamento
valorPao = 0.12 #o pão custa R$0,12
valorBroa = 1.50 #a broa custa R$1,50
margemPoupanca = 0.10 #o dono da padaria deseja guardar 10% do valor arrecado diariamente 

vendaPao = quantidadeDePao * valorPao
vendaBroa = quantidadeDeBroa * valorBroa
totalArrecado = vendaPao + vendaBroa
poupanca = totalArrecado * 0.10

# saída
print('HOJE, a padaria arrecadou R${:.2f}. O dono pode guardar na poupança R${:.2f} do valor arrecado!'.format(totalArrecado, poupanca))

