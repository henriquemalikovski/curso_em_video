from datetime import date

ano = int(input("Digite o ano: "))
if ano == 0:
    ano = int(date.today().year)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} É bixsesto".format(ano))
else:
    print("O ano {} NÃO É bixsesto".format(ano))
