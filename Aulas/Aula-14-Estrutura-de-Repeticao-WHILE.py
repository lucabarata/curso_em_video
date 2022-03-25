'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim.')
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim.')
r = 'S'
while r == 'S':
    n1 = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim.')'''
n2 = 1
par = impar = 0
while n2 != 0:
    n2 = int(input('Digite um número: '))
    if n2 != 0:
        if n2 % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')