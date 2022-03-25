nome = list()
nome.append('Luca')
nome.append(24)
lista_nomes = list()
lista_nomes.append(nome[:])
nome[0] = 'Joel'
nome[1] = 55
lista_nomes.append(nome)
print(lista_nomes)

galera = [['Joao', 24], ['Maria', 12], ['Renata', 14], ['Luis', 15]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')