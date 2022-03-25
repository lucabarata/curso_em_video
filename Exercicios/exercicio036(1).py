salario = float(input('Salário: R$'))
valor = float(input('Valor do imóvel: R$'))
minimo = (salario * 5/100) * 12
print('Para comprar o imóvel você precisaria de {:.2f} anos aplicando 5% de seu salário.'.format(valor / minimo))
