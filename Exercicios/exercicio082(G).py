lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    elif v % 2 == 1:
        lista_impar.append(v)
print('=-' * 30)
print(f'Lista de números: {lista}')
print(f'Lista de números pares: {lista_par}')
print(f'Lista de números ímpares: {lista_impar}')
