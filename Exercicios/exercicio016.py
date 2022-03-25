# crie um programa que leia um numero Real qualquer pelo teclado e mostre sua porcao inteira.
# import math
from math import trunc
num = float(input('Digite um número: '))
# print('O número {} tem como sua parte inteira o número {}'.format(num, math.trunc(num)))
# print(f'O número {num} tem como sua parte inteira o número {math.trunc(num)}')
# print(f'O número {num} tem como sua parte inteira o número {trunc(num)}')
print(f'O número {num} tem como sua parte inteira o número {int(num)}.')
