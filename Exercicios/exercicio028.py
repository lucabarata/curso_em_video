from random import randint
from time import sleep
cores = {'verde': '\033[32m',
         'verm:': '\033[31m',
         'limpa': '\033[m'}
a = randint(1, 2)
num = int(input('Sorteei um numero de 1 à 2. Advinhe qual é! '))
print('Então você acha que é o número {}?'.format(num))
sleep(2)
print('Tem certeza?')
sleep(2)
print('Você ainda pode mudar!')
sleep(2)
if num >= 3:
    print('Você é um idiota ou algo do tipo? \033[31;40mH\033[32ma\033[35mH\033[30ma\033[33mH\033[36ma\033[m')
if num == a:
    print('{}Você acertou!!!{}'.format(cores['verde'], cores['limpa']))
if num != a and num < 3:
    print('{}Você errou, tente de novo!!! Era o número {}!{}'.format(cores['verm:'], a, cores['limpa']))
