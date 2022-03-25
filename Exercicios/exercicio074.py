from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')
