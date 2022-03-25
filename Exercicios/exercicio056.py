maisvelho = 0
maisnovo = 0
masc = 0
fem = 0
for c in range(1, 5):
    print(f'- {c}ª Pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()
    if c == 1:
        maisvelho = idade
        maisnovo = idade
    else:
        if idade > maisvelho:
            maisvelho = idade
        if idade < maisnovo:
            maisnovo = idade
    if sexo == 'M':
        masc += 1
    if sexo == 'F':
        fem +=1
print(f'O mais velho tem {maisvelho} anos e o mais novo tem {maisnovo} anos.')
print(f'Nesse grupo possuem {masc} pessoas do sexo masculino e {fem} pessoas do sexo feminino.')