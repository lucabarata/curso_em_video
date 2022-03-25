num = int(input('Número da taboada: '))
print('=-'*6)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c:2}')
print('=-'*6)