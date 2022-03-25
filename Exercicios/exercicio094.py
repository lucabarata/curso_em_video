lista = list()
lista_f = list()
cadastro = dict()
c = soma = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    if cadastro['sexo'] == 'F':
        lista_f.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
    soma += cadastro['idade']
    c += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    if cont == 'N':
        break
media = soma / c
print(f'Foram cadastrados {len(lista)} pessoas')
print(f'Média das idades: {media}')
print(f'Lista mulheres: {lista_f}')
co = 0
print('Pessoas acima da méida de idade: ', end='')
for cs in lista:
    if lista[co]['idade'] > media:
        print(f'{lista[co]["nome"]}', end=' | ')
    co += 1

