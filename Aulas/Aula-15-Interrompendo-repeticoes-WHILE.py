n = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
print(f'Soma: {s}')
nome = 'José'
idade = 35
print(f'O {nome:-^20} tem {idade}.')
print(f'O {nome:->20} tem {idade}.')