totalPessoas = 3 #50

maiorAltura = 0
menorAltura = float('inf') #inicializar uma variável com o maior valor possível.
somaAlturas = 0

somaAlturaMulheres = 0
contMulheres = 0
contHomens = 0

for i in range(1, totalPessoas + 1):
    print(f"\nPessoa {i}")
    
    while True:
        try:
            altura = float(input('Informe a altura (em metros): '))
            if (altura <= 0):
                raise ValueError # instrução usada para lançar manualmente uma exceção
            break
        except:
            print('Altura inválida. Tente novamente.')
    
    while True:
        sexo = input('Informe o Sexo [0 = masculino, 1 = feminino): ')
        if sexo in ['0', '1']:
            sexo = int(sexo)
            break
        else:
            print('Sexo inválido. Digite 0 para masculino ou 1 para feminino.')
    
    somaAlturas += altura

    if (altura > maiorAltura):
        maiorAltura = altura
    if (altura < menorAltura):
        menorAltura = altura

    if (sexo == 1):
        somaAlturaMulheres += altura
        contMulheres += 1
    else:
        contHomens += 1

# cálculos finais
mediaGeral = somaAlturas / totalPessoas

if contMulheres > 0:
    mediaMulheres = somaAlturaMulheres / contMulheres
else:
    mediaMulheres = 0

percentualHomens = (contHomens / totalPessoas) * 100

print("\n{:=^40}".format(" RESULTADOS DA PESQUISA "))
print("a) Maior altura registrada   : {:.2f} m".format(maiorAltura))
print("   Menor altura registrada   : {:.2f} m".format(menorAltura))
print("{:-^40}".format(""))
print("b) Média de altura (mulheres): {:.2f} m".format(mediaMulheres))
print("c) Média de altura (geral)   : {:.2f} m".format(mediaGeral))
print("{:-^40}".format(""))
print("d) Percentual de homens      : {:.2f}%".format(percentualHomens))
print("="*40)



