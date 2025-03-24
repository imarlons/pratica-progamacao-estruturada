# EXERCÍCIO 08

# Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, 
# calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em dias;
# d) a idade dessa pessoa em semanas.

def calcularIdade():
    anoNascimento = int(input('Informe o seu ano de nascimento: '))
    anoAtual = int(input('Informe o ano atual: '))

    idadeAnual = anoAtual - anoNascimento
    idadeMensal = idadeAnual * 12
    idadeDiaria =  idadeAnual * 365 #não exite ano bissexto nesse programa
    idadeSemanal = idadeAnual * 52

    print('A sua idade em anos é {}'.format(idadeAnual))
    print('A sua idade em meses é {}'.format(idadeMensal))
    print('A sua idade em dias é {}'.format(idadeDiaria))
    print('A sua idade em semanas é {}'.format(idadeSemanal))

calcularIdade()

