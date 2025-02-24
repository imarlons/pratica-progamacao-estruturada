# EXERCÍCIO 03

# faça um programa que verifique se uma letra digitada é "F" ou "M". 
# conforme a letra escrever: F - feminino, M - masculino, sexo Inválido.

# entrada
letra = str(input('Digite F ou M: '))

# processamento & saída
if (letra.upper() == 'F'):
    print('F - Feminino')
elif (letra.upper() == 'M'):
    print('M - Masculino')
else:
    print('Sexo inválido!')

    
