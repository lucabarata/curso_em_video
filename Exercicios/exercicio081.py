lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    p = ' '
    while p not in 'SN':
        p = str(input('Continuar? [S/N]')).strip().upper()[0]
    if p in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado na {lista.index(5)}ª posição.')
else:
    print('O valor 5 não foi digitado.')
print(lista)