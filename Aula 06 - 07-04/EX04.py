# EXERCÍCIO 04

# escreva um programa que converta um intervalo de tempo dado em minutos, em horas, minutos e segundos. 
# por exemplo, se o tempo dado for 145.87 minutos, o programa deve fornecer 2 h 25 min 52,2 s.

tempoMin = float(input("Digite o tempo em minutos: "))

horas = int(tempoMin // 60)
minutos = int(tempoMin % 60)
segundos = (tempoMin - int(tempoMin)) * 60

print('{} h {} minutos {:.1f} segundos'.format(horas, minutos, segundos))
