# EXERCÍCIO 02

# um tonel de refresco é feito com 8 partes de água e 2 partes de suco de maracujá. 
# faça um algoritmo para calcular quantos litros de água e de suco 
# são necessários para se fazer X litros de refresco (informados pelo usuário).

def calcularIngredientes():
    litrosRefresco = float(input('Quantos litros de refresco deseja fazer? '))
    
    agua = (8 / 10) * litrosRefresco #80% do refresco / 8 partes
    suco = (2 / 10) * litrosRefresco #20% do refresco / 2 partes
    
    print('Para preparar {} litros de refresco, você precisará de:'.format(litrosRefresco))
    print('{:.2f} litros de água.'.format(agua))
    print('{:.2f} litros de suco.'.format(suco))

calcularIngredientes()

