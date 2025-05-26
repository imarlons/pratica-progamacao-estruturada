nome = input('Informe o seu nome: ')
contador = 0
for caracter in nome:
    if (caracter != ' '):
        contador += 1
print(contador)