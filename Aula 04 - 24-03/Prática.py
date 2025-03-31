nome = 'Marlon da Silva'

print(nome[:6]) # retorna 'Marlon'
print(nome[10:15]) # retorna 'Silva'

par = nome[::2]
print('Caracteres nos índices pares: {}'.format(par))
impar = nome[1::2]
print('Caracteres nos índices ímpares: {}'.format(impar))