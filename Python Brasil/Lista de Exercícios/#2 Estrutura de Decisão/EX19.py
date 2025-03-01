# EXERCÍCIO 19

# faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# observando os termos no plural a colocação do "e", da vírgula entre outros. 
# exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# entrada
numero = int(input('Digite um número menor que 1000: '))

# processamento
def decomporNumero(numero):
    if numero < 0 or numero >= 1000:
        return 'Número fora do intervalo permitido!'

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    if centenas > 0:
        partes.append('{} {}'.format(centenas, 'centena' if centenas == 1 else 'centenas'))
    
    if dezenas > 0:
        partes.append('{} {}'.format(dezenas, 'dezena' if dezenas == 1 else 'dezenas'))
    
    if unidades > 0:
        partes.append('{} {}'.format(unidades, 'unidade' if unidades == 1 else 'unidades'))

    return ' e '.join(', '.join(partes).rsplit(', ' , 1))


# testando com os números fornecidos
testes = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
testes.insert(0, numero)

# saída
for num in testes:
    print("\n{} = {}".format(num, decomporNumero(num)))
 