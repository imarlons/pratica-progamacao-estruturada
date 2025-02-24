# EXERCÍCIO 10

# faça um programa que pergunte em que turno você estuda. 
# peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# entrada
turno = str(input('Qual turno você estuda? \nDigite M para Matutino, V para Vespertino ou N para Noturno: '))

# processamento & saída
if (turno.upper() == 'M'):
    print('Bom dia!')
elif (turno.upper() == 'V'):
    print('Boa tarde!')
elif (turno.upper() == 'N'):
    print('Boa noite!')
else:
    print('Valor inválido!')