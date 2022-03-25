nome = input('Digite seu nome completo:').strip()
print(f'Seu nome em letras maiusculas é: {nome.upper()}')
print(f'Seu nome em letras minusculas é: {nome.lower()}')
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')))
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras.')
print(f'Seu segundo nome é {nome.split()[1]}')

