matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = s3coluna = maior2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Número [{l}][{c}]: '))
        matrix[l][c] = n
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            somapar += matrix[l][c]
    print()
print(f'Soma dos pares: {somapar}')
for l in range(0, 3):
    s3coluna += matrix[l][2]
print(f'Soma da terceira coluna: {s3coluna}')
for c in range(0, 3):
    if c == 0:
        maior2l = matrix[1][c]
    elif matrix[1][c] > maior2l:
        maior2l = matrix[1][c]
print(f'O maior da segunda linha: {maior2l}')