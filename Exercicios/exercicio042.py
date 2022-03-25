vd = '\033[32m'
l = '\033[m'
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    print('É possível formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print(f'{vd}equilátero.{l}')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'{vd}isóceles.{l}')
    else:
        print(f'{vd}escaleno.{l}')
else:
    print('Não é possível formar um triângulo.')
