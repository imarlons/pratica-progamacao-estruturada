quantidade = int(input('Quantos pessoas você deseja verificar a idade? '))

somaMaiores = 0
mediaMaiores = 0
idades = 0

for i in range(quantidade):
    idade = int(input(f'Informe a idade da {i + 1}ª pessoa: '))
    if (idade >= 18):
        somaMaiores += 1
        idades += idade

print('Das pessoas verificadas, {} são maiores de idade.'.format(somaMaiores))
print('Dentre os maiores, a média de idade é: {}'.format(idades / somaMaiores))

