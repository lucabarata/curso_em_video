valores = []
for c in range(0, 5):
    valores.append(int(input(f'{c+1} - Valor: ')))
print('x'*40)
print(f'Foram digitados os valores {valores}')
print(f'Maior valor: {max(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}', end=' ')
print(f'\nMenor valor: {min(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}', end=' ')
