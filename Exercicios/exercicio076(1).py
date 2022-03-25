lista = ('Abacate', 3.99, 'Banana', 4, 'Mamão', 5, 'Tangerina', 6.50, 'Limão', 2, 'Laranja', 4, 'Uva', 7, 'Melão', 5.99)
total = 0
print('-' * 40, f'\n{"Preço produtos":^40}')
print('-' * 40)
for pos in range(0, len(lista), 2):
    print(f'{lista[pos]:.<30}', f'R${lista[pos+1]:5.2f}')
    total += lista[pos+1]
print('-' * 40)
print(f'Total: R${total:.2f}')