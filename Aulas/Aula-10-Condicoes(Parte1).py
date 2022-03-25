import emoji
tempo = int(input('Tempo do carro: '))
if tempo <= 3:
    print('Carro novo!', emoji.emojize(':thumbsup:', use_aliases=True))
else:
    print('Carro velho!', emoji.emojize(':hankey:', use_aliases=True))
print('carro novo'if tempo <= 3else'carro velho')
nome = str(input('Qual o seu nome? '))
if nome == 'Luca':
    print('Você é um merda, {}!'.format(nome), emoji.emojize(':hankey:', use_aliases=True))
else:
    print('Olá, {}. Prazer em conhecê-lo!'.format(nome))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('Sua nota é {}. PARABÉNS! VOCÊ ESTÁ ACIMA DA MÉDIA!'.format(m))
else:
    print('Sua nota é {}. PARABÉNS! VOCÊ É UM MERDA! PARABÉNS!'.format(m))
