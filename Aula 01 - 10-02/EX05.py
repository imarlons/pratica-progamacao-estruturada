# EXERCÍCIO 05

# linha para separar as informações e facilitar a visulização do programa no terminal
linha = ('--------------------')
# entrada
nome = str(input('Qual o seu nome? ')).upper()
idade = int(input('Qual a sua idade? '))

# processamento 
diasDoAno = 365 
diasDeVida = idade * diasDoAno
print(linha)

# saída
print('{}, você já viveu {} dias!'.format(nome, diasDeVida))
print(linha)