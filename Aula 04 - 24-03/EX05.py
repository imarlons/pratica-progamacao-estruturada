# EXERCÍCIO 05

# faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
# a) o novo peso se a pessoa engordar 15% sobre o peso digitado;
# b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado

def calcularPeso():
    peso = float(input('Informe o seu peso: '))

    engordar = peso + (peso * 0.15)
    emagrecer = peso - (peso * 0.20)

    print('Se você não fechar a boca, o seu novo peso será {:.1f}kg'.format(engordar))
    print('MASSS se você seguir a dieta, o seu novo peso será {:.1f}kg'.format(emagrecer))

calcularPeso()

