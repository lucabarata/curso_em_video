print('PROGRESSÃO ARITMÉTICA')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1 + (10-1) * r
for c in range(a1, an + r, r):
    print('{}'.format(c), end=' → ')
print(f'Aritmética de razão {r} e primeiro termo {a1}: 10 primeiros termos.')