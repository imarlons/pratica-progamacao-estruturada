# EXERCÍCIO 08

# três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar.
# faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, 
# mas faça com que Carlos e André não paguem centavos. 
# ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para Felipe.

# entrada
valorConta = float(input('Qual o valor total da conta? R$'))

# processamento
divisaoInteira = valorConta // 3
restante = valorConta - (2 * divisaoInteira)

# saída
print('Carlos vai pagar R${:.2f}'.format(divisaoInteira))
print('André vai pagar R${:.2f}'.format(divisaoInteira))
print('Felipe vai pagar R${:.2f}'.format(restante))