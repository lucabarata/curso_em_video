num = int(input('Digite um número para saber se ele é um número primo: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(f'\n\033[mO número {num} foi divisível {tot} vezes,', end=' ')
if tot == 2:
    print('portanto é um número primo.')
else:
    print('portanto ele não é um número primo.')
