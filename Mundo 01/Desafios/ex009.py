num = int(input('Digite o numero para a tabuada: '))
x = 1
for x in range(11):
    r = num * x
    print('{} x {} = {}'.format(num, x, r))
    x += 1
