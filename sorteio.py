import random


listaDealunos = []
count = 0
while count <4:
    nomeDosalunos = str(input('Digite o nome dos alunos: '))
    listaDealunos.append(nomeDosalunos)
    count+=1
print('O aluno escolhido foi {}'.format(random.sample(listaDealunos,1)))