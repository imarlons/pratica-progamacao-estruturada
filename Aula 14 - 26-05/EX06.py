graos = 1  
totalGraos = graos

for i in range(2, 65):
    graos *= 2  
    totalGraos += graos  

print('A rainha precisará de {} grãos de trigo para pagar o monge.'.format(totalGraos))