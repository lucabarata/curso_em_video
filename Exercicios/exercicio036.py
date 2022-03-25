valor = float(input('Olá! Seja bem-vindo ao seu consultor financeiro digital!\n'
                    'Para começarmos, informe o valor do imóvel que deseja adquirir: R$'))
salario = float(input('Muito bem! Agora nos informe o seu salário, por favor. R$'))
tempo = float(input('Em quantos anos você deseja quitar o imóvel?'))
prestacao = valor / (tempo * 12)
minimo = salario * 30/100
print('A prestação mensal para seu imóvel seria de R${:.2f}'.format(prestacao))
if prestacao >= minimo:
    print('O empréstimo será negado devido à prestação exceder 30% do seu salário. Sinto muito.')
else:
    print('O seu empréstimo será aceito!')