from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho: '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nasc
for k, v in cadastro.items():
    print(f'{k} - {v}')