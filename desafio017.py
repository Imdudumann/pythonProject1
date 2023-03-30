from math import hypot

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input(('Digite o valor do cateto adjacente: ')))
print('O valor da hipotenusa é: {:.2f}'.format(hypot(catetoOposto,catetoAdjacente)))