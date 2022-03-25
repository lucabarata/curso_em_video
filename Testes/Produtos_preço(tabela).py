lista_nome = list()
lista_precos = list()
q = int(input('Quantidade de produtos que deseja cadastrar: '))
w = q
while True:
    lista_nome.append(str(input('Nome produto: ')).capitalize())
    q -= 1
    if q == 0:
        break
while True:
    lista_precos.append(float(input('Valor: ')))
    q += 1
    if q == w:
        break
for pos in range(0, len(lista_nome)):
    print(f'{pos + 1} - {lista_nome[pos]:.<30}', f'R${lista_precos[pos]:6.2f}')
