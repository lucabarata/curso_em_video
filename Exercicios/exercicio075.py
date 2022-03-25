a = int(input('Número: '))
b = int(input('Número: '))
c = int(input('Número: '))
d = int(input('Número: '))
tupla = (a, b, c, d)
print(f'Tupla: {tupla}')
if 9 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro número 3 digitado está {tupla.index(3)+1}ª posição')
pares = 0
for c in tupla:
    if c % 2 == 0:
        pares += 1
print(f'Foram digitados {pares} números pares')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
