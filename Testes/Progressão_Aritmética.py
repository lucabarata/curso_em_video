a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = int(input('Termos iniciais: '))
cont = 1
total = 0
while termos != 0:
    total += termos
    while cont <= total:
        print(f'{a1}', end=' > ')
        a1 += r
        cont += 1
    print('Pausa.')
    termos = int(input('Mais quantos termos? '))
print('*' * 40, '\n')
print(f'Foram contabilizados {total} termos.')