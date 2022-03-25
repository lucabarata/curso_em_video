escolha = 0
saldo = 10000
valor = 0
print('='*35)
print('Caixa Eletrônico Banco do Caralho')
print('='*35)
while escolha != 5:
    nota1 = nota2 = nota5 = nota10 = nota20 = nota50 = nota100 = nota200 = 0
    print('''[1] SAQUE
[2] SALDO
[3] DOE TODO SEU DINHEIRO AO BANCO
[4] FIQUE POBRE NOS DEIXE RICO
[5] ENCERRAR''')
    print('='*35)
    escolha = int(input('Opção: '))
    print('='*35)
    if escolha == 1:
        valor = int(input('Qual o valor que deseja sacar? R$'))
        print('='*35)
        saldo -= valor
        while True:
            while valor >= 200:
                nota200 += 1
                valor -= 200
            while valor >= 100:
                nota100 += 1
                valor -= 100
            while valor >= 50:
                nota50 += 1
                valor -= 50
            while valor >= 20:
                nota20 += 1
                valor -= 20
            while valor >= 10:
                nota10 += 1
                valor -= 10
            while valor >= 5:
                nota5 += 1
                valor -= 5
            while valor >= 2:
                nota2 += 1
                valor -= 2
            while valor >= 1:
                nota1 += 1
                valor -= 1
            if valor == 0:
                break
        if nota200 > 0:
            print(f'{nota200} cédula(s) de R$200,00')
        if nota100 > 0:
            print(f'{nota100} cédulas(s) de R$100,00')
        if nota50 > 0:
            print(f'{nota50} cédulas(s) de R$50,00')
        if nota20 > 0:
            print(f'{nota20} cédulas(s) de R$20,00')
        if nota10 > 0:
            print(f'{nota10} cédula(s) de R$10,00')
        if nota5 > 0:
            print(f'{nota5} cédula(s) de R$5,00')
        if nota2 > 0:
            print(f'{nota2} cédula(s) de R$2,00')
        if nota1 > 0:
            print(f'{nota1} cédula(s) de R$1,00')
        print('='*35)
    if escolha == 2:
        print(f'Saldo: R${saldo:.2f} ')
        print('='*35)
    if escolha == 3:
        print(f'Você doou R${saldo} ao Banco do Caralho! Obrigado! Se fode ai!')
        saldo = 0
        print('='*35)
    if escolha == 4:
        print('Você é retardado por acaso?')
        print('='*35)
