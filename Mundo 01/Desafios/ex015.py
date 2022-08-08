dias = int(input('Por quantos dias o carro foi alugado? '))
kms = float(input('Quantos km foram rodados? '))

valor = (dias * 60) + (kms * 0.15)

print('O valor a ser pago pelo aluguel do carro é: {:.2f}'.format(valor))
