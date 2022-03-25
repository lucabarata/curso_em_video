ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer contiuar?[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-' * 25)
print('{:<6}{:<15}{:>20}'.format('No.', 'Nome', 'Média'))
print('-' * 50)
for i, a in enumerate(ficha):
    print(f'{i:<6}{a[0]:<15}{a[2]:>20}')
while True:
    print('-' * 50)
    opc = int(input('Mostar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizado.')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte sempre! >>>')
