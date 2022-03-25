num = int(input('Número: '))
num_var = num
fator = num
fatorial = 1
while fator != 1:
    fatorial = num_var * (fator - 1)
    num_var = fatorial
    fator -= 1
print(f'O número {num} tem como seu fatorial: {num}! = {fatorial}')
n1 = num
print(f'{num}! = ', end='')
while n1 != 1:
    print(f'{n1} x', end=' ')
    n1 -= 1
print(f'1 = {fatorial}')

