from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'{k} - DADO: {v}')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=' * 25)
print('         == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'        {i+1}° lugar: {v[0]} - DADO: {v[1]}')
    sleep(1)