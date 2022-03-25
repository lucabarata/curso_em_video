maior_18 = 0
homens = 0
mulheres_menor_20 = 0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade > 18:
        maior_18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres_menor_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'''Mais de 18 anos: {maior_18}
Homens: {homens}
Mulheres com menos de 20 anos: {mulheres_menor_20}''')
