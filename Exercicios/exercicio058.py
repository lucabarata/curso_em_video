from random import randint
cores = {'verde': '\033[32m',
         'verm:': '\033[31m',
         'limpa': '\033[m'}
a = randint(1, 10)
print('Sorteei um numero de 1 à 10. Advinhe qual é! ')
num = 1
tentativas = 0
while num != a:
    num = int(input('Escolha: '))
    tentativas += 1
if num == a:
    print('{}Você acertou!!!{}'.format(cores['verde'], cores['limpa']))
print(f'Você precisou de {tentativas} tentativas para acertar o resultado.')
