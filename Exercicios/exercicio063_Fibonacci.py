# SOMENTE NÚMEROS PARES
# contador = metade do número de termos desejado
# alterar número de termos → print linha 8
print('\nSequência de Fibonacci v1.0')
print('='*63)
num = 1
num_anterior = 0
cont = 5
print('10 primeiros termos', end=' ')
while cont != 0:
    print(f'→ \033[31m{num_anterior}\033[m → {num}', end=' ')
    num_anterior += num
    num += num_anterior
    cont -= 1
print('')
print('='*63)

