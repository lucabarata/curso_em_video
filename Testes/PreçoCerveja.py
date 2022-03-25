lista = []
variavel = []
precos = []
while True:
    variavel.append(str(input('Nome da cerveja: ')))
    variavel.append(float(input('Digite o valor da cerveja: ')))
    variavel.append(float(input('Digite quantos mls: ')))
    lista.append(variavel[:])
    variavel.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?')).strip().upper()[0]
    if cont == 'N':
        break
print(lista)
for p in lista:
    print(f'{p[2]:.0f}ml - {p[0]:.<15}', f'R${p[1]:5.2f}')
print(precos)
