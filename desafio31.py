distancia = float(input('Digite qual a distância da sua viagem: '))
if distancia <=200:
    print('Essa viagem vai custar: {}$'.format(distancia*0.50))
else:
    print('Sua viagem vai custar: {}$'.format(distancia*0.45))