velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    dif = velocidade - 80
    valor = dif * 7
    print("Você foi multado em R$ {:.2f}".format(valor))
else:
    print("Você esta dentro do limite")
