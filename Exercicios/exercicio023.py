# numero = str(input('Digite um número:'))
# u = numero[3]
# d = numero[2]
# c = numero[1]
# m = numero[0]
# print(u, d, c, m)

n = int(input('Digite outro número: '))
print('Unidades: {}'.format(n % 10))
print(f'Dezenas: {n // 10 % 10}')
print(f'Centenas: {n // 100 % 10}')
print(f'Milhares: {n // 1000 % 10}')


