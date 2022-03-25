c = soma = mais_1000 = mais_barato = 0
nome_mais_barato = ''
while True:
    c += 1
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    print('x'*20)
    soma += valor
    if c == 1:
        nome_mais_barato = nome
        mais_barato = valor
    if valor < mais_barato:
        nome_mais_barato = nome
        mais_barato = valor
    if valor > 1000:
        mais_1000 += 1
    continua = str(input('Deseja continuar: ')).upper().strip()[0]
    print('x'*20)
    if continua in 'Nn':
        break
print(f'''Soma: R${soma:.2f}
Nome do produto mais barato: {nome_mais_barato}
Valor do produto mais barato: R${mais_barato:.2f}
Produtos acima de R$1000,00: {mais_1000}
Produtos cadastrados: {c}''')