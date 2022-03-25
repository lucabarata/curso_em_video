from datetime import date
nome = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho ("0" se não tem): '))
idade = date.today().year - nasc
if ctps != 0:
    anocontrat = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$'))
    aposent = (anocontrat + 35) - nasc
if ctps == 0:
    anocontrat = 0
    
cadastro = {'nome': {nome},
            'idade': {idade},
            'ctps': {ctps},
            'contratação': {anocontrat},
            'salário': {sal},
            'aposentadoria': {aposent}}

