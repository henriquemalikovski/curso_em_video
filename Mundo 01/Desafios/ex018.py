from math import tan, cos, sin, radians

angulo = float(input('Digite o angulo: '))

vSen = sin(radians(angulo))
vCos = cos(radians(angulo))
vTan = tan(radians(angulo))

print(
    'Para o angulo {}, o valor de seno é {:.2f}, de cosseno {:.2f} e tangente {:.2f}'.format(angulo, vSen, vCos, vTan))
