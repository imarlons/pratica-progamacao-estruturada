# linha para separar as informações e facilitar a visulização do programa no terminal
linha = ('--------------------')
print('--- FICHA CADASTRAL ---')
nomeCompleto = input('Informe seu nome completo: ')
idade = int(input('Informe a sua idade: '))
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a seu altura: '))
print(linha)
print('Olá, {}!'.format(nomeCompleto)) #{} + .format() é uma forma de apresentar os valores de forma mais organizada.
print('Você tem {} anos, pesa aproximadamente {:.2f}kg e tem {:.2f}m de altura.'.format(idade, peso, altura)) #{:.2f} é um recurso para definir o número de casas após a vírgula/ponto para valores flutuantes.
print(linha)
print('Você aparenta ser um bom canditado para o programa! \nAgradecemos o cadastro! Retornaremos em breve!')
print(linha)