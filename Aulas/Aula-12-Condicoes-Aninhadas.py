nome = str(input('Nome: '))
if nome == 'Luca':
    print('Feio')
elif nome == 'Joao' or nome == 'Paulo' or nome == 'Jose':
    print('Seu nome é popular.')
elif nome in 'Ana Maria Marcela Daniela Julia':
    print('Nome feminino.')
else:
    print('Nome comum.')
