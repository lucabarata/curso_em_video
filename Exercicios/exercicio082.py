lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? ')).strip().upper()[0]
    if p == 'N':
        break
print(f'Lista de números: {lista}')
print(f'Lista de números pares: {lista_par}')
print(f'Lista de números ímpares: {lista_impar}')