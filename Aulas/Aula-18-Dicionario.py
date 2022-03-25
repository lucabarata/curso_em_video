lista_cadastros = []
cadastro = {}
c = 0
while c < 2:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    cidade = str(input('Cidade: '))
    cadastro = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
    lista_cadastros.append(cadastro)
    c += 1
print('-'*25)
print(f'{"Nome":<10}{"Cidade":<10}{"Idade"}')
for p in lista_cadastros:
    print(f'{p["Nome"]:<10}{p["Cidade"]:<10}{p["Idade"]:^5}')
