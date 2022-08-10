from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

print('O valor da Hipotenusa é {:.2f}'.format(hypot(co, ca)))
