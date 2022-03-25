matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
somapar = tercoluna = maiorseglin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Número [{l}] [{c}]: '))
        maiorseglin = matrix[1][0]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            pares.append((matrix[l][c]))
            somapar += matrix[l][c]
        if c == 2:
            tercoluna += matrix[l][2]
        if l == 1:
            if matrix[l][c] > maiorseglin:
                maiorseglin = matrix[1][c]
    print()
print(pares)
print(f'A soma dos valores pares da matrix é {somapar}')
print(f'A soma dos valores da terceira coluna da matrix é {tercoluna}')
print(f'O maior elemento da segunda linha é {maiorseglin}')