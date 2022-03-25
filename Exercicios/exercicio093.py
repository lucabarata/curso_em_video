somgol = 0
gols = list()
dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Partidas: '))
for c in range(0, partidas):
    gol = int(input(f'Gols {c+1}ª partida: '))
    somgol += gol
    gols.append(gol)
    dados['gols'] = gols[:]
dados['total de gols'] = somgol
for k, v in dados.items():
    print(f'{k} - {v}')
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'{c+1}ª Partida: {gols[c]}')
print(f'Total de gols: {somgol}')
