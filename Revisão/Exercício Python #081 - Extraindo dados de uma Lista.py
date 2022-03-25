lista_numeros = []
while True:
    lista_numeros.append(int(input('Número: ')))
    print(lista_numeros)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? (S/N): ')).upper().strip()
    if cont == 'N':
        break
print(f'Foram digitados {len(lista_numeros)} números.')
lista_numeros.sort(reverse=True)
print(f'Os valores da lista em ordem crescente são: {lista_numeros}')
if 5 in lista_numeros:
    print('O valor "5" está na lista.')
else:
    print('O valor "5" não está na lista.')
