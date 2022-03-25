# Jokenpô
import random
from time import sleep
lista = [1, 2, 3]
escolha = random.choice(lista)

nome = str(input('Olá! Qual seu nome? '))
print(f'Muito prazer em conhecê-lo, {nome.capitalize()}!')
start = input('Vamos jogar Jokenpô!? ')
print('Tá bom! Então vamos!')
sleep(1)
print('Joo...')
sleep(0.8)
print('Ken...')
sleep(0.8)
print('Pôô!!')
sleep(0.8)
jogador = int(input('''
Pedra (1)
Tesoura (2)
Papel (3)\n
Escolha: '''))
print('Você jogou ', end='')
if jogador == 1:
    print('PEDRA')
elif jogador == 2:
    print('TESOURA')
elif jogador == 3:
    print('PAPEL')
else:
    print('Você tem problema?')
if escolha == jogador:
    print('Empate')
elif escolha == 1 and jogador == 2:
    print('Você perdeu!')
elif escolha == 1 and jogador == 3:
    print('Você ganhou!')
elif escolha == 2 and jogador == 3:
    print('Você perdeu!')
elif escolha == 2 and jogador == 1:
    print('Você ganhou!')
elif escolha == 3 and jogador == 1:
    print('Você perdeu!')
elif escolha == 3 and jogador == 2:
    print('Você ganhou!')
else:
    print('Você tem dificuldade mental.')
l = '\033[m'
vd = '\033[31m'
if escolha == 1:
    escolha = 'PEDRA'
elif escolha == 2:
    escolha = 'TESOURA'
elif escolha == 3:
    escolha = 'PAPEL'
print(f'Minha escolha foi {vd}{escolha}{l}!!')