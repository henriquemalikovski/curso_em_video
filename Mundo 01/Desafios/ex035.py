r1 = float(input("Digite o primeiro seguimento: "))
r2 = float(input("Digite o segundo seguimento: "))
r3 = float(input("Digite o terceiro seguimento: "))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print("Os seguimentos podem formar um triangulo")
else:
    print("Os seguimentos não podem formar um triangulo")
