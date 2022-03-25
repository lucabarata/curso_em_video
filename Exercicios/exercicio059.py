n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
num = 0
while num != 5:
    soma = n1 + n2
    multiplicacao = n1 * n2
    print('''------------------
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
------------------''')
    num = int(input('Opção: '))
    print('''------------------
Resultado:''')
    if num == 1:
        print(f'{n1} + {n2} = {soma}')
    if num == 3:
        if n1 > n2:
            print(f'O maior número é \033[32m{n1}\033[m')
        elif n1 == n2:
            print(f'Os números equivalem.')
        else:
            print(f'O maior número é \033[32m{n2}\033[m')
    if num == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))
    if num == 2:
        print(f'{n1} x {n2} = {multiplicacao}')
print('Programa finalizado.')
