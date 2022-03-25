pessoas = {'nome': 'Luca', 'sexo': 'másculino', 'idade': 24}
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos e sexo {pessoas["sexo"]}.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
# del pessoas['sexo']
pessoas['idade'] = 35
pessoas['peso'] = 70.2
for k, v in pessoas.items():
    print(f'{k} - {v}')