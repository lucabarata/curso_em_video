numeros = []
while True:
    n = int(input('Número: '))
    if n in numeros:
        print('Número já existente na lista.')
    else:
        numeros.append(n)
    p = ' '
    while p not in 'SN':
        p = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if p in 'N':
        break
numeros.sort()
print(numeros)
