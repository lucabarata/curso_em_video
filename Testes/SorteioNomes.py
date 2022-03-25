import random
from random import choice
lista_de_nomes = ['Luca', 'Marcos', 'Ronaldo', 'Renata', 'Ana', 'Camila']
print(f'Seu nome será {choice(lista_de_nomes)}.', end=' ')

lista_paises = ['Brasil', 'Italia', 'India', 'China', 'Japão', 'Holanda']
pais = random.choice(lista_paises)
print(f'Seu país será {pais}', end=' ')
lista_cidades_brasil = ['São Paulo', 'Sao Tomé das Letras', 'Campo Grande']
lista_cidades_italia = ['Cerveno', 'Brescia', 'Roma']
lista_cidades_india = ['Délhi', 'Calcuta', 'Mumbai']
lista_cidades_china = ['Xangai', 'Pequim', 'Cantao']
lista_cidades_japao = ['Tokyo', 'Osaka', 'Quioto']
lista_cidades_holanda = ['Amsterdã', 'Roterdã', 'Haia']
lista_cidades = [lista_cidades_brasil, lista_cidades_italia, lista_cidades_india, lista_cidades_china,
                 lista_cidades_japao, lista_cidades_holanda]
print('e você será de', end=' ')
if pais == lista_paises[0]:
    print(choice(lista_cidades_brasil))
if pais == lista_paises[1]:
    print(choice(lista_cidades_italia))
if pais == lista_paises[2]:
    print(choice(lista_cidades_india))
if pais == lista_paises[3]:
    print(choice(lista_cidades_china))
if pais == lista_paises[4]:
    print(choice(lista_cidades_japao))
if pais == lista_paises[5]:
    print(choice(lista_cidades_holanda))
