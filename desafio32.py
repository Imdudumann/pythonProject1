ano = float(input('Digite um ano para saber se ele é bissexto: '))
divi = ano % 4
if divi == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto')