salario = float(input("Digite o seu salário: "))

if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.10

print("Seu salário passa a ser R$ {:.2f}".format(salario))
