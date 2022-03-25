print('{:*^50}'.format(' TOP 10 PIB RANKING '))
pibrank = ('EUA', 'CHINA', 'JAPÃO', 'ALEMANHA', 'REINO UNIDO', 'ÍNDIA', 'FRANÇA', 'ITÁLIA', 'CANADÁ', 'CORÉIA')
for c, pais in enumerate(pibrank):
    print(f'{c+1:2} - {pais}')
print('{:*^50}'.format(' TOP 5 PIB RANKING '))
for c in range(0, 5):
    print(f'{c+1:2} - {pibrank[c]}')
print('{:*^50}'.format(' LAST 5 TOP 10 '))
for c in range(5, 10):
    print(f'{c + 1:2} - {pibrank[c]}')
print('{:*^50}'.format(' ORDEM ALFABÉTICA DOS PAÍSES '))
print(sorted(pibrank))

print('Itália está na ', pibrank.index('CANADÁ'), end='')
print('ª posição.')
