total = 0
lista = ('Abacate', 3.99, 'Banana', 4, 'Mamão', 5, 'Tangerina', 6.50, 'Limão', 2, 'Laranja', 4, 'Uva', 7, 'Melão', 5.99)
print('-' * 40, f'\n\033[32m{"Lista de preços":^40}\033[m')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'\033[33m{lista[pos]:.<30}\033[m', end='')
    else:
        total += lista[pos]
        print(f'\033[32mR${lista[pos]:5.2f}\033[m')
print('-' * 40)
print(f'Total: R${total:.2f}')
