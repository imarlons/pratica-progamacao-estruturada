# EXERCÍCIO 05

# um usuário deseja um algoritmo onde possa escolher que tipo de média deseja
# calcular a partir de 3 notas. Faça um algoritmo que leia as notas, 
# a opção escolhida pelo usuário e calcule a média.
# ● aritmética
# ● ponderada (3,3,4)

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

print('\nQual média você deseja calcular?')
print('[ 1 ] - Aritmética \n[ 2 ] - Ponderada (Pesos: 3, 3, 4)')
opcao = int(input('Para continuar, digite 1 ou 2: '))

if (opcao == 1):
    media = (nota1 + nota2 + nota3) / 3
    print('Média Aritmética: {}'.format(media))
elif (opcao == 2):
    media = (nota1 * 3 + nota2 * 3 + nota3 * 4)  / 10
    print('Média Ponderada: {}'.format(media))
else:
    print('Opção inválida!')