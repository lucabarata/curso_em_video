lista_np = []
lista_tot = []
maiorpeso = 0
menorpeso = 0
while True:
    lista_np.append(str(input('Nome: ')))
    lista_np.append(float(input('Peso: ')))
    if len(lista_tot) == 0:
        menorpeso = maiorpeso = lista_np[1]
    else:
        if lista_np[1] > maiorpeso:
            maiorpeso = lista_np[1]
        if lista_np[1] < menorpeso:
            menorpeso = lista_np[1]
    lista_tot.append(lista_np[:])
    lista_np.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {len(lista_tot)} pessoas.')
print(f'O maior peso encontrado foi {maiorpeso:.2f}Kg referente à ', end='')
for p in lista_tot:
    if p[1] == maiorpeso:
        print(f'{p[0]}', end='/ ')
print(f'\nO menor peso encontrado foi {menorpeso:.2f}Kg referente à ', end='')
for p in lista_tot:
    if p[1] == menorpeso:
        print(f'{p[0]}', end='/ ')