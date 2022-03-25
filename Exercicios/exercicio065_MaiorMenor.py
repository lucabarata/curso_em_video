cont = som = num = maior = menor = 0
p = ''
while p != 'N':
    num = int(input('Digite um número: '))
    som += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    p = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print(f'''Digitados: {cont}
Média: {som / cont}
Maior: {maior}
Menor: {menor}''')