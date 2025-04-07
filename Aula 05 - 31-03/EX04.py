# EXERCÍCIO 04

# um banco concederá um crédito especial aos seus clientes, variável com o saldo
# médio no último ano. Faça um algoritmo que leia o saldo médio de um cliente e
# calcule o valor do crédito de acordo com a tabela abaixo. Mostre uma mensagem
# informando o saldo médio e o valor do crédito.

# saldo médio  | percentual
# de 0 a 200   | nenhum crédito
# de 201 a 400 | 20% do valor do saldo médio
# de 401 a 600 | 30% do valor do saldo médio
# acima de 601 | 40% do valor do saldo médio

saldoMédio = float(input('Informe o seu saldo médio: R$'))

if (saldoMédio > 0 and saldoMédio <= 200):
    print('Saldo Médio: R${:.2f} \nVocê não tem acesso a crédito especial!'.format(saldoMédio))
elif (saldoMédio > 200 and saldoMédio <= 400): 
    credito = saldoMédio * 0.20
    print('Saldo Médio: R${:.2f} \nCrédito: R${:.2f}'.format(saldoMédio, credito))
elif (saldoMédio > 200 and saldoMédio <= 600): 
    credito = saldoMédio * 0.30
    print('Saldo Médio: R${:.2f} \nCrédito: R${:.2f}'.format(saldoMédio, credito))
elif (saldoMédio > 600): 
    credito = saldoMédio * 0.40
    print('Saldo Médio: R${:.2f} \nCrédito: R${:.2f}'.format(saldoMédio, credito))
else:
    ('Insira a informação corretamente!')

    