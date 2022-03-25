soma_idade = 0
mais_velho = 0
mulheres_menor_20 = 0
homem_mais_velho = 0
for c in range(1, 5):
    print('-' * 5, f'{c}ª pessoa', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    soma_idade += idade
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    if sexo == 'M':
        if c == 1:
            mais_velho = idade
            homem_mais_velho = nome
        else:
            if idade > mais_velho:
                mais_velho = idade
                homem_mais_velho = nome
media_idade = soma_idade / 4
print('-' * 21)
print(f'A média das idades do grupo é igual à {media_idade}.')
print(f'{homem_mais_velho} é o homem mais velho e sua idade é {mais_velho}.')
if mulheres_menor_20 == 0:
    print('Não existem mulheres com idade abaixo de 20 anos no grupo.')
else:
    print(f'Existem {mulheres_menor_20} mulheres abaixo dos 20 anos no grupo.')
