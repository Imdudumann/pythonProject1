primeiroLado = float(input('Digite o primeiro lado do triângulo: '))
segundoLado = float(input('Digite o segundo lado do triângulo: '))
terceiroLado = float(input('Digite o terceiro lado do triângulo: '))
if primeiroLado + segundoLado > terceiroLado:
    print('Não é um triângulo!')
if primeiroLado + terceiroLado > segundoLado:
    print('Não é um triângulo!')
if segundoLado + terceiroLado > primeiroLado:
    print('Não é um triângulo!')
