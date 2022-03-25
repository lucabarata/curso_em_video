from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
print('Você tem {} e sua categoria será: '.format(atual - ano), end='')
if atual - ano <= 9:
    print('CATEGORIA MIRIM')
elif atual - ano <= 14:
    print('CATEGORIA INFANTIL')
elif atual - ano <= 19:
    print('CATEGORIA JUNIOR')
elif atual - ano <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
