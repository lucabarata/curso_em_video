indiv = []
notas = []
todos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    indiv.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    indiv.append(notas[:])
    indiv.append(media)
    notas.clear()
    todos.append(indiv[:])
    indiv.clear()
    cont = ' '
    if cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 20)
print(' No.    NOME                  MÉDIA')
print('-' * 40)
for n, p in enumerate(todos):
    print(f' {n:<7}{p[0]:<22}{p[2]:>1.2f} ')
print('-' * 40)
while True:
    escolha = int(input('Mostrar nota de qual aluno? '))
    if escolha == 999:
        break
    if escolha <= len(todos) - 1:
        print(f'Notas {todos[escolha][0]}: {todos[escolha][1]}'
              f'\nMédia {todos[escolha][0]}: {todos[escolha][2]}')
print('-' * 40)
