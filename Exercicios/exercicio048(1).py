soma = 0
cont = 0
print('Números ímpares múltiplos de 3 entre 0 e 500: ', end=' ')
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        print(c, end=' ')
print(' ')
print(f'A somatória de números ímpares múltiplos de 3 no invervalo de 0 à 500 é \033[31;52m{soma}\033[m!')
print(f'A quantidade de númeors ímpares e múltiplos de 3 nesse intervalo é: \033[31m{cont}\033[m')