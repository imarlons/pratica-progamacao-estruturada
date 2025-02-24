# EXERCÍCIO 04

# faça um programa que verifique se uma letra digitada é vogal ou consoante.

# entrada
letra = str(input('Digite uma letra: '))

# processamento 
vogais = ['A', 'E', 'I', 'O', 'U']

for vogal in vogais:
    if letra.upper() == vogal:
        print('A sua letra é uma vogal!') 
        break
    else:
        print('A sua letra é uma consoante!') 
        break