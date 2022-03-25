lista_n = []
maior = menor = 0
for c in range(0, 5):
    lista_n.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista_n[c]
    else:
        if lista_n[c] > maior:
            maior = lista_n[c]
        if lista_n[c] < menor:
            menor = lista_n[c]
print(f'Lista de números digitados: {lista_n}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, v in enumerate(lista_n):
    if v == maior:
        print(f'{p} ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, v in enumerate(lista_n):
    if v == menor:
        print(f'{p} ', end='')
print()
