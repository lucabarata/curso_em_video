# style: 0 = none
# style: 1 = bold
# style: 4 = underline
# style: 7 = negative
# text: 30 = branco
# text: 31 = vermelho
# text: 32 = verde
# text: 33 = amarelo
# back: 40 = branco
# back: 41 = vermelho
# back: 42 = verde
# back: 43 = amarelo
# \033(0;33;44m)
nome = 'Luca'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'brancoepreto': '\033[7m'}
print('Olá, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
