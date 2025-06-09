nHabitantes = int(input('Quantos habitantes vão participar da pesquisa? '))

contador = 0
somaSalarios = 0
somaFilhos = 0
maiorSalario = 0
salario100 = 0

for i in range(nHabitantes):
    salario = float(input(f'Informe o salário do {i + 1}º habitante: R$'))
    if (salario < 0):
        break

    filhos = int(input(f'Informe a quantidade de filhos do {i + 1}º habitante: '))

    somaSalarios += salario
    somaFilhos += filhos
    contador += 1

    if (salario > maiorSalario):
        maiorSalario = salario
    if (salario <= 100):
        salario100 += 1

if (contador > 0):
    mediaSalario = somaSalarios / contador
    mediaFilhos = somaFilhos / contador
    percentual = (salario100 / contador) * 100

    print('\n===== RESULTADO DAS PESQUISAS =====')
    print('A média de salário da população é: R${:.2f}'.format(mediaSalario))
    print('A média de filhos da população é: {:.2f} filhos(as)'.format(mediaFilhos))
    print('O maior salário da população é: R${:.2f}'.format(maiorSalario))
    print('O percentual de habitantes com salário até R$100 é: {:.2f}%'.format(percentual))
else:
    print('Nenhum dado válido foi inserido.')
