km = float(input("Digite os kms da viagem: "))

if km > 200:
    valorKM = 0.45
else:
    valorKM = 0.50

valorViagem = km * valorKM

print("A viagem custará R$ {:.2f}".format(valorViagem))
