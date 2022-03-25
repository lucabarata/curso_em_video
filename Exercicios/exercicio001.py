print('Digite seus dados: ')
nome = str(input('Nome: '))
estciv = str(input('Estado civil: '))
idade =str(input('Idade: '))
CEP = str(input('CEP: '))
endereco = str(input('Endereço: '))
numero = str(input('Numero: '))
bairro = str(input('Bairro: '))
cidade = str(input('Cidade: '))
pais = str(input('País: '))
# print('Nome: ', nome, '\n', estciv, '\n', idade, '\n', CEP, '\n', endereco, ',', numero, '\n', bairro, '\n', cidade,
#       '\n', pais)
# lista = nome, estciv, idade, CEP, endereco, numero, bairro, cidade, pais
# print(lista)

print(f'Nome: {nome}\nEstado civil: {estciv}\nIdade: {idade}\nCEP: {CEP}\nEndereço: {endereco},'
      f'\nBairro: {bairro}\nCidade: {cidade}\nPais: {pais}'.split())
