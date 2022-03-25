n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Núemro 3: '))
if n3 < n1 > n2:
    print('Número 1: {} é o maior.'.format(n1))
if n3 < n2 > n1:
    print('Número 2: {} é o maior.'.format(n2))
if n2 < n3 > n1:
    print('Número 3: {} é o maior.'.format(n3))
if n3 > n1 < n2:
    print('Número 1: {} é o menor.'.format(n1))
if n3 > n2 < n1:
    print('Número 2: {} é o menor.'.format(n2))
if n2 > n3 < n1:
    print('Número 3: {} é o menor.'.format(n3))
