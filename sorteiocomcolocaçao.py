import random

listaDealunos = []
contador = 0
while contador <4:
    nomedosAlunos = str(input('Digite o nome dos alunos: '))
    listaDealunos.append(nomedosAlunos)
    contador+=1
random.shuffle(listaDealunos)
print(listaDealunos)