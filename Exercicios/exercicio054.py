from datetime import date
tot2 = 0
tot = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade  = atual - ano
    if idade < 18:
        tot += 1
    else:
        tot2 += 1
print(f'{tot} pessoas são menor de idade.')
print(f'{tot2} pessoas são maior de idade.')

