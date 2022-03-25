from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
escolha_computador = itens[computador]
print('=-' * 20)
print('{:^40}'.format('JOKENPÔ'))
print('=-' * 20)
print('''Escolha:
(1) Pedra
(2) Papel
(3) Tesoura''')
escolha = int(input('Opção: '))
if escolha == 1:
    escolha = 'Pedra'
elif escolha == 2:
    escolha = 'Papel'
elif escolha == 3:
    escolha = 'Tesoura'
else:
    print('Você é retardado?')
print('=-' * 20)
sleep(0.8)
print('Jóóó...')
sleep(0.8)
print('Ken...')
sleep(0.8)
print('Pôô!')
sleep(0.8)
print('=-' * 20)
if escolha == escolha_computador:
    print('Empate!')
elif escolha == 'Pedra' and escolha_computador == 'Tesoura':
    print('Você ganhou!')
elif escolha == 'Pedra' and escolha_computador == 'Papel':
    print('Você perdeu!')
elif escolha == 'Papel' and escolha_computador == 'Tesoura':
    print('Você perdeu!')
elif escolha == 'Papel' and escolha_computador == 'Pedra':
    print('Você ganhou!')
elif escolha == 'Tesoura' and escolha_computador == 'Pedra':
    print('Você perdeu!')
elif escolha == 'Tesoura' and escolha_computador == 'Papel':
    print('Você ganhou!')
print(f'Sua escolha foi {escolha}!')
print(f'A escolha do computador foi {itens[computador]}!')

