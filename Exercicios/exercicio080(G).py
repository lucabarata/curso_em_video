lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                print(f'Valor adicionado na posição {p}')
                break
            p += 1
print('=-' * 30)
print(f'A lista de números em ordem crescente é {lista}')