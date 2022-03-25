import math
import emoji
import random

# math
# ceil > arrendonda para cima
# floor > arredonda para baixo
# trunc > truncar numero
# pow > power, potencia
# sqrt > raiz quadrada, square root

n3 = float(random.randint(0, 10))
n2 = random.random()
# n = float(input('digite um numero:'))
ceil = math.ceil(n2)
floor = math.floor(n2)
n4 = n3 + n2
print('random randit:', n2)
print('random random:', n3)
print('ceil:', ceil)
print(n4)
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Nós acabamos por aqui! :thumbs_up:'))