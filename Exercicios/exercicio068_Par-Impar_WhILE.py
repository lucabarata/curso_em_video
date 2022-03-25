from random import randint
c = 0
while True:
    escolha_pc = randint(1, 5)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha par ou ímpar: ')).strip().upper()[0]
    num = 6
    while num > 5:
        num = int(input('Escolha 1 - 5: '))
    soma = escolha_pc + num
    print(f'Você jogou {num} e o computador jogou {escolha_pc} somando {soma}!')
    if escolha == 'P' and soma % 2 == 0:
        print('Você ganhou! A soma foi PAR!')
    elif escolha == 'I' and soma % 2 == 1:
        print('Você ganhou! A soma foi IMPAR!')
    else:
        print('Você perdeu!')
        break
    c += 1
print(f'Vitórias consecutivas: {c}')