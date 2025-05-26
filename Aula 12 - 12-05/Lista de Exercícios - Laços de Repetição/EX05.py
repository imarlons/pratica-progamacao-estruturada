candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo5 = 0
branco6 = 0

for v in range(1, 7):
    voto = int(input('Informe o seu voto: '))

    if (voto == 1):
        candidato1 += 1
    elif (voto == 2):
        candidato2 += 1
    elif (voto == 3):
        candidato3 += 1
    elif (voto == 4):
        candidato4 += 1
    elif (voto == 5):
        nulo5 += 1
    elif (voto == 6):
        branco6 += 1
    else:
        print('O valor informado não foi computado!')

print('========== APURAÇÃO DOS VOTOS ==========')
print('''Candidato 1: {} voto(s)
         Candidato 2: {} voto(s)
         Candidato 3: {} voto(s)
         Candidato 4: {} voto(s)
         Nulo       : {} voto(s)
         Branco     : {} voto(s)
      '''.format(candidato1, candidato2, candidato3, candidato4, nulo5, branco6))


