v = '\033[31m'
vd = '\033[32m'
li = '\033[m'
preco = float(input('Preço do produto: '))
condicao = int(input(f'''Escolha como deseja efetuar o pagamento:
-À vista {vd}dinheiro/cheque{li}: 10% de desconto (1)
-À vista no {vd}cartão{li}: 5% de desconto (2)
-Em até {vd}2x no cartão{li}: Preço normal (3)
-{vd}3x ou mais{li} no cartão: 20% de juros (4)
Digite o número de referência para fazer a opção.
Opção: '''))
preco1 = preco - (preco * 0.1)
preco2 = preco - (preco * 5/100)
preco3 = preco
if condicao < 4:
    print(f'''Preço do produto: R${vd}{preco}{li}
Preço total:''', end=' ')
    if condicao == 1:
        print(f'{vd}R${preco1:.2f}')
    elif condicao == 2:
        print(f'{vd}R${preco2:.2f}')
    elif condicao == 3:
        print(f'{vd}R${preco3:.2f}')
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    if parcelas < 3:
        print(f'Preço total: {preco:.2f}')
    elif parcelas >= 3:
        preco4 = preco + (preco * 20 / 100)
        precoparcela = preco4 / parcelas
        print(f'Preço do produto: R${vd}{preco}{li}\n'
              f'Preço total: {v}R${preco4:.2f}{li}\n'
              f'Quantidade de parcelas: {v}{parcelas}{li}\n'
              f'Preço parcela: R${v}{precoparcela:.2f}{li}\n')
