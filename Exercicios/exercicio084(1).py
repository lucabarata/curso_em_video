temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
