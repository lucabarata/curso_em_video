num = [6, 4, 7, 1, 9]
num[1] = 2
num.append(6)
num.insert(1, 5)
num.pop(0)

if 6 in num:
    num.remove(6)
else:
    print('Número 6 não encontrado na lista.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

