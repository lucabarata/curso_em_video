alimento = ('Vatapá', 'Churrasco', 'Macarrão', 'Camarão', 'Abacate')
print(alimento)
# for c in alimento:
#    print(f'{c}', end=', ')
# for count in range(0, len(alimento)):
#     print(alimento[count], end=', ')
# for c in range(0, len(alimento)):
#    print(f'{c} - {alimento[c]}')
for c, comida in enumerate(alimento):
    print(f'{c} - {comida}')
print(sorted(alimento))
a = (1, 3, 5, 7)
b = (2, 4, 6, 8)
c = a + b
print(sorted(c))
print(len(c))
print(c.count(5))
print(c.index(1))

