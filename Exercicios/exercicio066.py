s = c = n = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'''Digitados: {c}
Somatória: {s}''')
