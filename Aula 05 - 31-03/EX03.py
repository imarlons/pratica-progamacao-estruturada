# EXERCÍCIO 03

# tendo como dados de entrada:
# ● a altura
# ● e o sexo de uma pessoa (‘M’ masculino e ‘F’ feminino)

# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# ● para homens: (72.7*h)-58
# ● para mulheres: (62.1*h)-44.7

altura = float(input('Informe a sua altura: '))
sexo = str(input('Informe o seu sexo, sendo "M" para Masculino e "F" para Feminino: '))

if (altura > 0):
    if (sexo.upper() == 'M'):
        pesoIdeal = (72.7 * altura) - 58
        print('O seu peso ideal é {:.1f}kg'.format(pesoIdeal))
    elif (sexo.upper() == 'F'):
        pesoIdeal = (62.1 * altura) - 44.7
        print('O seu peso ideal é {:.1f}kg'.format(pesoIdeal))
else:
    print('Insira as informações corretamente!')

