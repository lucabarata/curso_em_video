time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        cont = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Use somente "S" ou "N".')
    if cont == 'N':
        break
print('=-'*30)
print(f'{"COD":<3}{"NOME":>15}{"GOLS":>15}{"TOTAL":>15}')
print('-'*50)
for i, j in enumerate(time):
    print(f'{i:>3}{j["nome"]:>15}{str(j["gols"]):>15}{str(j["total"]):>15}')
print('=-' * 30)
while True:
    escolha = int(input('(999 para parar) COD: '))
    print('=-'*30)
    if escolha == 999:
        break
    if escolha >= len(time):
        print('ERRO! Jogador não encontrado.')
        print('=-'*30)
    else:
        print(f'Jogador: {time[escolha]["nome"]}')
        for i, g in enumerate(time[escolha]['gols']):
            print(f'{i+1}ª partida: {g} gols')
        print('=-'*30)
print('Programa encerrado.')