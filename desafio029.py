velo = int(input('Digite a velocidade do carro: '))
vMulta = velo - 80
custoMulta = vMulta * 7
if velo > 80:
    print('Você foi multado!')
    print('Você terá que pagar {}$ pelos km exedidos!'.format(custoMulta))
else:
    print('Você está dentro do limite!')