# EXERCÍCIO 06

# a empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. 
# faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário. 
# considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

# entrada
cargaHoraria = int(input('Quantas horas você trabalha normalmente? '))
trabalhoExtra = input('Você fez hora extra? (S/N) ')

cargaExtra = 0

if(trabalhoExtra.upper() == 'S'):
    cargaExtra = int(input('Quantas horas extra você fez? '))


# processamento
valorHora = 10
valorHoraExtra = 15

salarioBruto = cargaHoraria * valorHora + cargaExtra * valorHoraExtra
salarioLiquido = salarioBruto - (salarioBruto * 0.1)

# saída
print('O salário bruto do funcionário é R${:.2f} e o liquído será R${:.2f}, pois foi descontado 10% dos impostos.'.format(salarioBruto, salarioLiquido))
