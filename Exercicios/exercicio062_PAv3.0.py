print('Progressão aritmética versão 3.0')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
an = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{an}', end=' > ')
        an += r
        cont += 1
    print('PAUSA...')
    mais = int(input('Mais quantos termos? '))
print(f'Foram contabilizados {total} termos nessa progressão aritmética.')
