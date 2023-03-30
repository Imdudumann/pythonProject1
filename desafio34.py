sal = float(input('Digite quanto você ganha: '))
if sal > 1.250:
    print('Você vai receber um aumento de {}'.format(sal*10/100))
else:
    print('Você vai receber um aumento de {}'.format(sal*15/100))