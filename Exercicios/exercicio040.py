am = '\033[33m'
vd = '\033[32m'
l = '\033[m'
v = '\033[31m'
print('''Média: < 5 - \033[31mREPROVADO\033[m
Média: > 5 e < 7 - {}RECUPERAÇÃO{}
Média: >= 7 - {}APROVADO{}'''.format(am, l, vd, l))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Média: {v}{media:.2f}{l}', end=' - ')
    print(f'{v}REPROVADO{l}')
elif media >= 5 and media < 7:
    print(f'Média: {am}{media:.2f}{l}', end=' - ')
    print(f'{am}RECUPERAÇÃO{l}')
else:
    print(f'Média: {vd}{media:.2f}{l}', end=' - ')
    print(f'{vd}APROVADO!{l}')
