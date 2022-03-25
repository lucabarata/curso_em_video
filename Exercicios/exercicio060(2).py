n = int(input('Número: '))
c = n
f = 1
for x in range(n, 0, -1):
    print(x, end='')
    print(' x ' if x > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)
