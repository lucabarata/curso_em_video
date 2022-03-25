print('SOMA DE NÚMEROS PARES ')
cont = 0
soma = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor : '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Quantidade de números pares: {cont}')
print(f'Soma de números pares: {soma}')