# programa para calcular a soma S = 1/1 + 1/2 + 1/3 + ... + 1/n
n = int(input('digite um valor inteiro e positivo para n: '))

if (n <= 0):
    print('o valor de n deve ser inteiro e positivo.')
else:
    S = 0.0
    for i in range(1, n + 1):
        S += 1 / i
    print('a soma S é: {:.2f}'.format(S))
