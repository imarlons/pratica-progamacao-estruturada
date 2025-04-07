# EXERCÍCIO 03

# crie um algoritmo que leia quatro valores digitados pelo usuário: n, a, b, c.
# a) Se n = 1 imprimir os três valores a, b, c em ordem crescente.
# b) Se n = 2 escrever os três valores a, b, c em ordem decrescente.
# c) Se n = 3 escrever os três valores a, b, c de forma que o maior fique no meio

n = int(input("Digite o valor de N (1, 2 ou 3): "))
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

valores = [a, b, c]

if n == 1:
    # ordem crescente
    valores.sort()
    print('Ordem Crescente: {}'.format(valores))

elif n == 2:
    # ordem decrescente
    valores.sort(reverse = True)
    print('Ordem Decrescente: {}'.format(valores))

elif n == 3:
    # maior valor no meio
    maior = max(valores)
    valores.remove(maior)
    resultado = [valores[0], maior, valores[1]]
    print('Maior Valor no Meio: {}'.format(resultado))
else:
    print("Valor de N é inválido. Use 1, 2 ou 3.")


