from datetime import date
print('Digite ¨0¨ para informar o ano atual.')
ano = int(input('Ano: '))
if ano == 0:
    ano = date.today().year
print('Ano: {}'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\33[32mBISSEXTO\33[m')
else:
    print('\33[31mNão BISSESTO')
