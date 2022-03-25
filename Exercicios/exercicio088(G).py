from random import randint
from time import sleep
temp = []
princ = []
print('-' * 30)
print('     JOGO NA MEGA SENA       ')
print('-' * 30)
jogos = int(input('Quantos jogos você quer sortear? '))
tot = 0
while tot < jogos:
    c = 0
    while True:
        n = randint(0, 60)
        if n not in temp:
            temp.append(n)
            c += 1
        if c == 5:
            break
    temp.sort()
    princ.append(temp[:])
    temp.clear()
    tot += 1
print('=-' * 5, f'SORTEANDO {jogos} JOGOS', '=-' * 5)
for i, l in enumerate(princ):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)