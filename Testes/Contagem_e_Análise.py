play = ''
lista = []
somatoria_valor = 0
somatoria_peso = 0
while play != 'ENCERRAR':
    nome_do_produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    peso = float(input('Peso do produto: '))
    lista += nome_do_produto
    somatoria_valor += valor
    somatoria_peso += peso
    play = str(input('Deseja continuar a registrar? (Se deseja encerrar, digite: ¨encerrar¨)')).strip().upper()
print(f'A somatória dos valores é igual à R${somatoria_valor:.2f}.')
print(f'A somatória dos pesos é igual à {somatoria_peso} gramas')
print(f'{lista[1]}')