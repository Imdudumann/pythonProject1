from random import randint
from time import sleep

randomico = randint(0,10)
minhaTentativa = int(input('Digite um número para saber se você acertou: '))
print('-'*10,'PROCESSANDO','-'*10)
sleep(2)
if minhaTentativa == randomico:
    print('Você acertou!')
else:
    print('Tente de novo!')
    print('O número randomico sorteado foi {}'.format(randomico))