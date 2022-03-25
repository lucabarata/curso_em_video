for c in range(0, 5):  # 1
    print('Vai tomar no cú!')
print('~' * 10, '1')
for c in range(0, 10+1):  # 2
    print(c)
print('~' * 10, '2')
for c in range(0, 11, 2):  # 3
    print(c)
print('~' * 10, '3')
i = int(input('Inicio: '))  # 4
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('~' * 10, '4')
for c in range(0, 6):  # 5
    n = input('Digite um número:')
print('~' * 10, '5')
s = 0  # 6
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
