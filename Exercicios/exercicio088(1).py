from random import randint
from time import sleep
princ = []
listan = []
x = int(input('Quantos jogos você deseja jogar? '))
for c in range(0, x):
    while len(listan) != 6:
        n = randint(0, 60)
        if n not in listan:
            listan.append(n)
        listan.sort()
    princ.append(listan[:])
    listan.clear()
for c in range(0, x):
    print(f'{c+1} - {princ[c]}')
    sleep(1)