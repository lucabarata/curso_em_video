from random import randint
dados = dict()
lista = []
for c in range(0, 4):
    jogada = randint(1, 6)
    dados = {'Jogada': jogada}
    lista.append(dados)
