while True:
    n = int(input('Número da taboada: '))
    if n < 0:
        break
    print('=-' * 6)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c:2}')
    print('=-'*6)
