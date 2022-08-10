from random import randint

x = 0
lista = []
for x in range(4):
    aluno1 = input('Digite o nome do Aluno: ')
    lista.append(aluno1)

n = randint(0, 3)
print('Aluno sorteado é {}'.format(lista[n]))
