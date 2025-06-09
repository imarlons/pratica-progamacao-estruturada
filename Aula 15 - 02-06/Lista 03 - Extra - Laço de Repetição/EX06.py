quantidade = int(input('Quantos números você deseja somar? '))
soma = 0
for i in range(quantidade):
    numero = int(input(f'Informe o {i + 1}º número: '))
    soma += numero

print('A soma dos números informados é: {}'.format(soma))