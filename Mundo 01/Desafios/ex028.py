from random import randint
from time import sleep

n = randint(1, 5)

nu = int(input("Digite um numero: "))
print("Processando...")
sleep(3)

if nu == n:
    print("Você acertou!!!")
else:
    print("Você Errou!")
