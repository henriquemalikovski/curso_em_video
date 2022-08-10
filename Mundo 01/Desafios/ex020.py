from random import shuffle

x = 0
alunos = []
for x in range(4):
    aluno = input('Digite o nome do Aluno: ')
    alunos.append(aluno)

shuffle(alunos)

print('A lista de apresentação é {}'.format(alunos))
