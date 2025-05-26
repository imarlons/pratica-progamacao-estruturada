contador = 0
somaPares = 0

while contador <= 500:
    if (contador % 2 == 0):
        somaPares += contador
    
    contador += 1

print(somaPares)   
