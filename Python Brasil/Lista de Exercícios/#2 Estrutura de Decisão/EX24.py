# EXERCÍCIO 24

# faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# o resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

# entrada
numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
print('\nadição = + \nsubtração = - \nmultiplicação = * \ndivisão = /')
operacao = input('\nQual operação você deseja realizar? ')

# processamento
if (operacao == '+'):
    operacao = 'ADIÇÃO'
    resultado = numero1 + numero2
elif (operacao == '-'):
    operacao = 'SUBTRAÇÃO'
    resultado = numero1 - numero2
elif (operacao == '*'):
    operacao = 'MULTIPLICAÇÃO'
    resultado = numero1 * numero2
elif (operacao == '/'):
    operacao = 'DIVISÃO'
    resultado = numero1 / numero2
else:
    print('Operação inválida! Escolha entre " + - * / "')

if (resultado % 2 == 0):
    fraseA = 'PAR'
else:
    fraseA = 'ÍMPAR'

if (resultado > 0):
    fraseB = 'POSITIVO'
elif (resultado == 0):
    fraseB = 'NULO'
else:
    fraseB = 'NEGATIVO'

if (resultado == round(resultado)):
    fraseC = 'INTEIRO'
else:
    fraseC = 'DECIMAL'

# saída
print('\nOs números fornecidos foram {:.2f} e {:.2f}, a operação escolhida foi {}'.format(numero1, numero2, operacao))
print('\nO resultado da operação escolhida é {:.2f}'.format(resultado))
print('\nO número é {}, {} e {}!'.format(fraseA, fraseB, fraseC))
