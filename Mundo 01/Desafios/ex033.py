n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))
n3 = int(input("Digite o numero 3: "))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("O MENOR numero é {}".format(menor))
print("O MAIOR numero é {}".format(maior))
