valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

a = [2, 3, 5, 7]
b = a[:]
b.append(3)
b[2] = 3
print(a)
print(b)