# calcular a soma:
# soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
# padrão identificado:
# numerador: números ímpares de 1 até 99.
# denominador: números de 1 até 50.

numerador = 1
soma = 0

for denominador in range(1, 51):
    soma += numerador / denominador
    numerador += 2

print("A soma é: {:.2f}".format(soma))
