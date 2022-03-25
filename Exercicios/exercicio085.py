par = []
impar = []
for c in range(0, 7):
    numero = int(input(f'{c+1} - Digite um número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
todos = par + impar
todos.sort()
print(f'Você digitou os números: {todos}')
print(f'Os números pares são: {sorted(par)}')
print(f'Os números ímpares são: {sorted(impar)}')